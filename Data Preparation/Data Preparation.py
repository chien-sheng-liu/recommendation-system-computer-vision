# import relevant packages
import pandas as pd
import jenkspy


# initialize binning method for transactions
def binning_data(filepath):
    data = pd.read_csv(filepath, sep='|', encoding='utf-8')
    print(data.columns)
    # create click bin
    for column in data:
        if data[column].dtype == 'int64' and column.lower().find('id') == -1:
            column_name = str(column + '_bins')
            bin = jenkspy.jenks_breaks(data[column], nb_class=5)
            print(bin)
            bin[1] = (bin[1] + 0.1)
            label = [str(column + '_{}'.format(x)) for x in range(5)]
            data[column_name] = pd.cut(data[column], bins=bin, labels=label, include_lowest=True)
    # write result to repo
    return data


# read data
data_binning = binning_data(r'Dataset\transactions.csv')
data_binning.to_csv(r'Dataset\Prepared Dataset\transaction_bins.csv', index=False)
