"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(param_dict):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_
    """

    authenticator = IAMAuthenticator('VYsko8rFoH8FpZGmR0-BC_qnwmqPVVGRhRORUkmv1ORt')
    cloudant = CloudantV1(authenticator=authenticator)
    cloudant.set_service_url('https://fc608087-c224-4d6d-a4f0-5f070d63d66f-bluemix.cloudantnosqldb.appdomain.cloud')
    
    response = cloudant.post_all_docs(db='dealerships', include_docs=True,).get_result()

    return response


