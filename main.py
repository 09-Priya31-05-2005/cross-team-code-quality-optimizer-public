import json

from analyzer.analyzer import analyze_file


result = analyze_file(
    "test_code/sample.py"
)

print(
    json.dumps(
        result,
        indent=2
    )
)