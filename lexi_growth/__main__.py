import sys
from dotenv import load_dotenv
from lexi_growth.handlers.filter_handler import handle_word_filter
from lexi_growth.handlers.merge_handler import handle_word_merge_to_known_list
from lexi_growth.utils.arg_unit import args_to_kwargs

def main():
    load_dotenv()

    args = sys.argv

    if len(args) < 2:
        print("need args!")
        sys.exit(1)

    if "--merge" in args:
        handle_word_merge_to_known_list()

    if "--filter" in args:
        filter_index = args.index("--filter")
        handle_word_filter(**args_to_kwargs(args[filter_index + 1:]))

if __name__ == "__main__":
    main()
