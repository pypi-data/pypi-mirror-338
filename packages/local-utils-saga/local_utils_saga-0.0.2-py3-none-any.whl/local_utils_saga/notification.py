import httpx
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="a+")

logger = logging.getLogger(__name__)

def notify_scene_service(result={}):
    """Notify scene service about the completed asset sheet using FastAPI's httpx"""
    print("starting notify")

    callback_url = result.get("callback_url")

    print(callback_url, result)
    logger.info(f"Callback URL received: {callback_url}")

    if not callback_url:
        logger.error("No callback URL provided in request headers")
        return

    # Ensure callback URL has protocol, defaulting to https://
    if not callback_url.startswith(('http://', 'https://')):
        callback_url = f"https://{callback_url}"
        logger.info(f"Added HTTPS protocol to callback URL: {callback_url}")

    endpoint = f"{callback_url}/api/v1/assets/setAsset"
    logger.info(f"Final endpoint URL: {endpoint}")

    payload = {
        "status": result.get("status", "error"),
        "assetId": result.get("asset_id", "unknown"),  # Try both formats
        "assetName": result.get("assetName") or result.get("asset_name", "unnamed"),  # Try both formats
        "userId": result.get("userId") or result.get("user_id", "unknown"),  # Try both formats
        "properties": {
            "prompt": result['properties'].prompt,
            "style": result['properties'].style,
            "workflow": result['properties'].workflow
        },
    }

    logger.info(f"Notifying scene service for asset {payload['assetId']}")
    logger.debug(f"Notification payload: {payload}")

    try:
        response = httpx.post(
                endpoint,
                json=payload,
                timeout=30.0
            )

        if response.status_code != 200:
            logger.error(f"Failed to notify scene service. Status: {response.status_code}, Response: {response.text}")
        else:
            logger.info(f"Successfully notified scene service for asset {payload['assetId']}")
            logger.debug(f"Scene service response: {response.text}")

    except httpx.TimeoutException:
        logger.error("Timeout while notifying scene service")
    except httpx.RequestError as e:
        logger.error(f"Network error notifying scene service: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error notifying scene service: {str(e)}")