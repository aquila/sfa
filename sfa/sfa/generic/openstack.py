from sfa.generic import Generic
from sfa.generic.pl import pl
import sfa.managers.aggregate_manager
import sfa.managers.registry_manager_openstack
import sfa.managers.slice_manager
import sfa.openstack.nova_driver
import sfa.server.sfaapi


# use pl as a model so we only redefine what's different
class openstack (pl):
    
    # the importer class
    def importer_class (self): 
        import sfa.importer.openstackimporter
        return sfa.importer.openstackimporter.OpenstackImporter
        
    # the manager classes for the server-side services
    def registry_manager_class (self) : 
        return sfa.managers.registry_manager_openstack.RegistryManager
    def aggregate_manager_class (self) :
        return sfa.managers.aggregate_manager.AggregateManager

    # driver class for server-side services, talk to the whole testbed
    def driver_class (self):
        return sfa.openstack.nova_driver.NovaDriver



