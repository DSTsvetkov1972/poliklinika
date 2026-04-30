from dotenv import load_dotenv
import os 

load_dotenv('.config')
print(os.getenv('ZETTA_PASSWORD'))