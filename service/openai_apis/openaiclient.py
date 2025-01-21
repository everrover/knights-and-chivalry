import os
from openai import OpenAI

# check if all environment variables are set
if not os.environ.get('OPENAI_API_KEY'):
  print('Error: No API key found')
  exit(1)
print('API_KEY:', os.environ.get('OPENAI_API_KEY'))

# load_dotenv()
API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)