import src.extractor as extractor
import src.processor as processor
def main():
    stock_data=extractor.extract_data()
    stock_data=processor.prepare_data_for_prophet(stock_data)
    print(stock_data["AAPL"])
    return 0




if __name__ == "__main__":
    main()