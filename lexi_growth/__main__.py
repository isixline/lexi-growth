from lexi_growth.application.lexi_flow_handler import handle_lexi_flow

def main():
    word_items = handle_lexi_flow("Hello, World lexi_flow subscriber!")
    for word_item in word_items:
        print(word_item)

if __name__ == "__main__":
    main()
