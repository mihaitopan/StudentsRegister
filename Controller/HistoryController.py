class AddOperation:
    """
    Class that models an add operation in the controller 
    """
    def __init__(self, Object):
        """
        Constructor for AddOperation class
        Object - The object that was added
        """
        self.__Object = Object
        
    def getObject(self):
        return self.__Object
    
class RemoveOperation:
    """
    Class that models a remove operation in the controller 
    """
    def __init__(self, Object):
        """
        Constructor for RemoveOperation class
        Object - The object that was removed
        """
        self.__Object = Object
        
    def getObject(self):
        return self.__Object
        
class UpdateOperation:
    """
    Class that models an update operation in the controller 
    """
    def __init__(self, oldObject, updatedObject):
        """
        Constructor for UpdateOperation class
        oldObject - The instance before updating
        updatedObject - The instance after the update
        """
        self.__oldObject = oldObject
        self.__updatedObject = updatedObject
        
    def getOldObject(self):
        return self.__oldObject

    def getUpdatedObject(self):
        return self.__updatedObject
    
class BatchRemoveOperation:
    
    def __init__(self, parent_object, affected_objects):
        '''
        parent_object - the object that caused the batch / cascade removal
        affects_objects - the objets that were deleted because of the parent_object deletion
        '''
        self.__parent_object = parent_object
        self.__affected_objects = affected_objects
        
    @property
    def parent_object(self):
        
        return self.__parent_object
    
    @property
    def affected_objects(self):
        
        return self.__affected_objects