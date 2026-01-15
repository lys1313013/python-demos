
ids = ['1', '2', '3', '4', '5', '6', '7']
batch = 3
for i in range(0, len(ids), batch):
    print(f"i: {i}")
    batch_ids = ids[i: i + batch]
    print(batch_ids)