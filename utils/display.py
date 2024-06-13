def generate_table(data):
    if len(data) == 0:
        print("No data available")
        return

    headers = list(data[0].keys())

    max_widths = [max(len(str(item[key])) for item in data + [{key: key}]) for key in headers]

    print("+" + "+".join("-" * (width + 2) for width in max_widths) + "+")
    print("| " + " | ".join(f"{header:<{max_widths[i]}}" for i, header in enumerate(headers)) + " |")
    print("+" + "+".join("-" * (width + 2) for width in max_widths) + "+")

    for row in data:
        print("| " + " | ".join(f"{row[key]:<{max_widths[i]}}" for i, key in enumerate(headers)) + " |")
        print("+" + "+".join("-" * (width + 2) for width in max_widths) + "+")

