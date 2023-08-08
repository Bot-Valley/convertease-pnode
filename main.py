import uvicorn, argparse
from contextlib import asynccontextmanager

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--standalone', action="store_true")
    args = parser.parse_args()

    if args.standalone:
        print("running standalone node")
        uvicorn.run("standalone.server:app", port=8000, reload=True)
    else:
        print("running cluster node")