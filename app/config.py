class Config:
    '''
    General configuration parent clas
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with General configutation settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True