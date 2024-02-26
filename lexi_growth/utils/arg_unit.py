
def args_to_kwargs(args):
    kwargs = {}
    for arg in args:
        key, value = arg.split("=")
        kwargs[key] = value
    print(f"kwargs: {kwargs}")
    return kwargs