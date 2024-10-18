from dotenv import load_dotenv
import os
load_dotenv()

settings = {key: value for key, value in os.environ.items()}

# for k, v in settings.items():
#     print(f'{k}={v}')
print(settings.get('DATABASE_USERNAME'))

