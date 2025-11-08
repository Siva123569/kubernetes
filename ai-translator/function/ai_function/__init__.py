import azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Azure Cognitive Services credentials
key = "<YOUR_TEXT_ANALYTICS_KEY>"
endpoint = "<YOUR_TEXT_ANALYTICS_ENDPOINT>"

credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        text = req_body.get('text')
        if not text:
            return func.HttpResponse("No text provided", status_code=400)

        # Summarize text (or any AI feature)
        response = client.extract_summary([text])[0]
        summary = response.summary if response else "Could not summarize"

        return func.HttpResponse(f'{{"summary": "{summary}"}}', mimetype="application/json")

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
