from client import PartialJSONCompleter

stream_chunk = '{"items": ["apple", "banana"'
res = PartialJSONCompleter.complete_json(stream_chunk)
print("Auto-completed object:", res["parsed"])
