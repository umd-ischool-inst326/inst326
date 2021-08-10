def pytest_json_runtest_metadata(item, call):
    if call.when == "setup":
        docstr = item.function.__doc__
        if docstr is None:
            docstr = ""
        out = {
            "name": docstr.strip(),
            "number": getattr(item.function, "number", ""),
            "max_score": getattr(item.function, "points", "1")
        }
        if hasattr(call, "excinfo"):
            out["output"] = str(call.excinfo)
            out["score"] = 0.0
        return out
