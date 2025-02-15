
class Extract:

    def __init__(self , branch):
        self.phase = "Extract"
        self.branch = branch

    def init_data_extract(self):
        print("Extract Data")

class Transform:

    def __init__(self, branch):
        self.phase = "Transform"
        self.branch = branch
        self.lookup_file = "Product_Mapping.csv"

    def init_data_transform(self):
        print("Transform Data")

class Load:

    def __init__(self, branch, database, user):
        self.phase = "Load"
        self.branch = branch
        self.db = database
        self.user = user

    def init_data_load(self):
        print("Load Data")

class ETL_Facade:

    def __init__(self, branch, database , user):
        self.extract = Extract(branch)
        self.transform = Transform(branch)
        self.load = Load(branch, database , user)


    def run_batch(self):
        self.extract.init_data_extract()
        self.transform.init_data_transform()
        self.load.init_data_load()


run_ETL_batch_Austria = ETL_Facade('AT' , 'DB_WH', 'FACADE')
run_ETL_batch_Austria.run_batch()
