import sys
import json

def block_ads(request):
    if "ads" in request["url"]:
        request["blocked"] = True
    else:
        return {"blocked": False}
     
def main():
    while True:
        message = sys.stdin.readline()
        if not message:
            break
        request = json.loads(message)
        response=block_ads(request)
        sys.stdout.write(json.dumps(response)+"\n")
        sys.stdout.write(json.dumps(response)+"\n")
        sys.stdout.flush()
    
if __name__ == "__main__":
    main()
