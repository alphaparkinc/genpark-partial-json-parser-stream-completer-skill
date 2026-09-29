"""Partial JSON Parser & Stream Completer.
100% Python Standard Library.
"""

import json

class PartialJSONCompleter:
    """Auto-completes in-flight truncated JSON streams into valid parseable JSON."""
    @staticmethod
    def complete_json(truncated_str: str) -> dict:
        s = truncated_str.strip()
        if not s:
            return {"parsed": {}, "was_completed": True}

        open_curly = s.count('{') - s.count('}')
        open_bracket = s.count('[') - s.count(']')
        in_quote = (s.count('"') % 2 == 1)

        completed = s
        if in_quote:
            completed += '"'

        if completed.rstrip().endswith(':'):
            completed += ' null'

        completed += ']' * max(0, open_bracket)
        completed += '}' * max(0, open_curly)

        try:
            data = json.loads(completed)
            return {"parsed": data, "completed_raw": completed, "was_completed": completed != s}
        except Exception as e:
            return {"parsed": None, "error": str(e), "raw": completed}
