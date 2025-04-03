from google.cloud import billing_v1
from google.cloud import bigquery
from google.cloud import recommender
from google.oauth2 import service_account


class GCPReservationCost:
    def __init__(self, project_id, credentials_path):
        self.project_id = project_id
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.billing_client = billing_v1.CloudBillingClient(credentials=self.credentials)
        self.bigquery_client = bigquery.Client(credentials=self.credentials, project=project_id)
        self.recommender_client = recommender.RecommenderClient(credentials=self.credentials)
        self.recommender_id = "google.compute.instanceReservations.Recommender"

    def get_billing_account(self):
        """Fetches the billing account ID for the given project"""
        project_name = f"projects/{self.project_id}"
        billing_info = self.billing_client.get_project_billing_info(name=project_name)
        return billing_info.billing_account_name if billing_info.billing_enabled else None

    def get_reservation_cost(self, start_date=None, end_date=None):
        """
        Fetches reservation cost data from BigQuery billing exports.
        Requires billing exports to be enabled in BigQuery.
        """
        billing_account = self.get_billing_account()
        if not billing_account:
            return {"error": "Billing is not enabled or accessible for this project."}

        if not start_date or not end_date:
            from datetime import datetime, timedelta
            today = datetime.today()
            start_date = today.replace(day=1).strftime("%Y-%m-%d")
            next_month = today.replace(day=28) + timedelta(days=4)
            end_date = next_month.replace(day=1) - timedelta(days=1)
            end_date = end_date.strftime("%Y-%m-%d")

        query = f"""
        SELECT service.description, sku.description, cost
        FROM `YOUR_BILLING_PROJECT_ID.YOUR_DATASET_ID.YOUR_TABLE_ID`
        WHERE usage_start_time BETWEEN TIMESTAMP('{start_date}') AND TIMESTAMP('{end_date}')
        AND sku.description LIKE '%Reservation%'
        """

        query_job = self.bigquery_client.query(query)
        results = query_job.result()

        return [dict(row) for row in results]

    def get_reservation_recommendation(self):
        """Fetches reservation recommendations from the GCP Recommender API."""
        parent = f"projects/{self.project_id}/locations/global/recommenders/{self.recommender_id}"
        recommendations = []

        try:
            response = self.recommender_client.list_recommendations(parent=parent)
            for recommendation in response:
                recommendations.append({
                    "id": recommendation.name,
                    "description": recommendation.description,
                    "impact": recommendation.primary_impact.category,
                    "savings": recommendation.primary_impact.cost_projection.cost
                    if recommendation.primary_impact.cost_projection else None,
                    "currency": recommendation.primary_impact.cost_projection.cost.currency_code
                    if recommendation.primary_impact.cost_projection else None,
                    "resource": recommendation.content.overview.get("recommendedReservation", {})
                })
            return {"recommendations": recommendations}

        except Exception as e:
            return {"error": f"Failed to fetch reservation recommendations: {str(e)}"}
