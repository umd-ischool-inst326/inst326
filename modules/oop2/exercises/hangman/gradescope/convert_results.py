from argparse import ArgumentParser
import json
import sys


def main(infile, outfile):
    with open(infile, "r", encoding="utf-8") as f:
        data = json.load(f)
    response = {}
    errors = []
    for collector in data["collectors"]:
        if collector["outcome"] == "failed":
            errors.append(collector["longrepr"])
    if errors:
        response["score"] = 0
        response["output"] = ("<p>The following errors were encountered:</p>\n"
                              "<pre>"+"\n----\n".join(errors)+"</pre>")
    tests = []
    for test in data["tests"]:
        out = {
            "score": (test["metadata"]["max_score"]
                      if test["outcome"] == "passed" else 0),
            "max_score": test["metadata"]["max_score"],
            "name": test["metadata"]["name"],
            "number": test["metadata"]["number"],
        }
        if "setup" in test and "crash" in test["setup"]:
            out["output"] = test["setup"]["crash"]["message"]
        elif "call" in test and "crash" in test["call"]:
            out["output"] = test["call"]["crash"]["message"]
            out["extra_data"] = {"long_output": test["call"]["longrepr"]}
        tests.append(out)
    tests.sort(key=lambda x: [int(n) for n in x["number"].split(".")])
    if tests:
        response["tests"] = tests
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(response, f)
        

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("infile", help="pytest json output")
    parser.add_argument("outfile", help="gradescope json file to write")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.infile, args.outfile)
