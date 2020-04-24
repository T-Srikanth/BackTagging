from oci.core import ComputeClient
from oci.exceptions import ServiceError
from oci.pagination import list_call_get_all_results
import Config


class Instance:
    def __init__(self):
        config = {}
        signer = Config.signer
        self.compute_client = ComputeClient(config=config, signer=signer)

    # Request to list all volume attachments
    def list_volume_attachments(self, compartment_id):
        try:
            return list_call_get_all_results(self.compute_client.list_volume_attachments,
                                             compartment_id).data
        except ServiceError as identifier:
            print(identifier.message)
            exit()

    def list_boot_volume_attachments(self, ad, compartment_id):
        return list_call_get_all_results(self.compute_client.list_boot_volume_attachments, ad,
                                         compartment_id).data

    def get_instance_details(self, instance_id):
        try:
            instance_data = self.compute_client.get_instance(instance_id).data
        except Exception as e:
            print("Instance ID is incorrect")
        return instance_data

    # gets the instance tag and caches the instance tags to reduce number of request

    def get_instance_tags(self, instance_id):
        instance_details = self.compute_client.get_instance(instance_id).data
        tags = dict()
        tags["defined_tags"] = instance_details.defined_tags
        tags["freeform_tags"] = instance_details.freeform_tags
        return tags
