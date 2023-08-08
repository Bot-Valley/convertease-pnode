# convertease-pnode
A converter node for the convertease api


# Installing dependencies
1. Create a virtual enviroment `python3 -m venv env`
2. Enter virtual enviroment
    1. Unix (linux/MacOS) `source /env/bin/activate`
    2. Windows `.\env\Scripts\activate`
3. Install dependencies `pip install -r requirements.txt`

# Run standalone node
1. `uvicorn main:app --reload`

# Run cluster node
1. `python main.py`