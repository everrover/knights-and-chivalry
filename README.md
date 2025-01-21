# knights-and-chivalry

A plugin for posting #InterviewPreparation using agentic-workflows

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# run fastapi server
uvicorn main:app --reload --port 8000
```

### Main end-points

- `/post/dsa`: Post a question's solution