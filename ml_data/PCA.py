import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
import helper
# import os

# projectpath = os.getcwd()
# print(projectpath)

def visual_2D_dataset(dataset_X, dataset_y, title):
    '''将二维数据集dataset_X和对应的类别dataset_y显示在散点图中'''
    assert dataset_X.shape[1] == 2, 'only support dataset with 2 features'
    classes = list(set(dataset_y))
    markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8'
        , 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|']
    # colors=['b','c','g','k','m','w','r','y']
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
              'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
    for class_id in classes:
        one_class = np.array([feature for (feature, label) in
                              zip(dataset_X, dataset_y) if label == class_id])
        plt.scatter(one_class[:, 0], one_class[:, 1], marker=markers[class_id % len(markers)],
                    c=colors[class_id % len(colors)], label='cls_' + str(class_id))
    plt.title(title)
    plt.legend()

# def pca(filepath):
#     dataset = helper.Helper.ReadPCAdata(filepath)
#     # # print(np.mat(dataset['pcadata'][0]))
#     samples = dataset['samples']
#     waves = ['wavelength' + str(i) for i in range(1, dataset['waves']+1)]
#     data = pd.DataFrame(columns=[*samples], index=waves)
#     # print(data.index)
#     i = 0
#     for wave in data.index:
#         data.loc[wave, 'A-1-2':'E-16-3'] = np.mat(dataset['pcadata'][i])
#         i = i + 1
#     print(data.head())
#     print(data.shape)
#
#     # Perform PCA on the data
#     # First center and scale the data
#     scaled_data = preprocessing.scale(data.T)
#
#     # print(scaled_data)
#     pca = PCA()  # create a PCA object
#     pca.fit(scaled_data)  # do the math
#     pca_data = pca.transform(scaled_data)  # get PCA coordinates for scaled_data
#
#     # # Draw a scree plot and a PCA plot
#     # # The following code constructs the Scree plot
#     per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
#     # print(per_var)
#     labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
#     plt.bar(x=range(1,len(per_var)+1), height=per_var, tick_label=labels)
#     plt.ylabel('Percentage of Explained Variance')
#     plt.xlabel('Principal Component')
#     plt.title('Scree Plot')
#     # plt.savefig("./images/img1.png"
#     plt.show()
#
#     # the following code makes a fancy looking plot using PC1 and PC2
#     pca_df = pd.DataFrame(pca_data, index=[*samples], columns=labels)
#     # print(pca_df)
#     plt.scatter(pca_df.PC1, pca_df.PC2)
#     plt.title('My PCA Graph')
#     plt.xlabel('PC1 - {0}%'.format(per_var[0]))
#     plt.ylabel('PC2 - {0}%'.format(per_var[1]))
#     for sample in pca_df.index:
#         plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
#     plt.savefig("./images/img1.png")
#     plt.show()
#
#     # Determine which genes had the biggest influence on PC1
#     # get the name of the top 10 measurements (wavelength) that contribute most to pc1.
#     # first, get the loading scores
#     loading_scores = pd.Series(pca.components_[0], index=waves)
#     # now sort the loading scores based on their magnitude
#     sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)
#     # get the names of the top 10 genes
#     top_10_genes = sorted_loading_scores[0:10].index.values
#     # print the gene names and their scores (and +/- sign)
#     print(loading_scores[top_10_genes])
#
#     dataset = {}
#     # print(pca_df)
#     for index, row in pca_df.iterrows():
#         dataset[str(index)] = [row['PC1'], row['PC2'], '']
#
#     import xlrd
#     filepath1 = '/Users/skye/Desktop/化学成分表格.xls'
#     data = xlrd.open_workbook(filepath1)
#     table = data.sheet_by_index(0)
#     for i in range(1, table.nrows):
#         list = dataset.get(str(table.row_values(i)[1]))  # note:column index is 1
#         # print(str(table.row_values(i)[1]))
#         if list:
#             list[2] = table.row_values(i)[12]
#
#     print(dataset)
#     return dataset

def pca1(data_path, prediction=False):
    import pandas as pd
    df = pd.read_csv(data_path, header=None)
    # print(df)
    rowNum = df.shape[0]  # 不包括表头
    colNum = df.columns.size

    dataset = df.values
    tmp = dataset[0:5][:,1:].transpose()
    samples = dataset[0]
    samples = samples[1:]
    samples = samples.tolist()
    # print(samples)
    waves = ['wavelength ' + str(i) for i in dataset[:,0][5:].tolist()]
    data = pd.DataFrame(columns=[*samples], index=waves)
    i = 5
    for wave in data.index:
        data.loc[wave, dataset[0][1]:dataset[0][-1]] = np.mat(dataset[i][1:])
        i = i + 1
    # print(data.head())
    print(data.shape)
    scaled_data = preprocessing.scale(data.T)
    pca = PCA()
    pca.fit(scaled_data)
    pca_data = pca.transform(scaled_data)
    per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
    print(per_var)
    labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]
    plt.bar(x=range(1, len(per_var) + 1), height=per_var, tick_label=labels)
    # plt.bar(x=range(1, 11), height=per_var[:10], tick_label=labels[:10])
    plt.ylabel('Percentage of Explained Variance')
    plt.xlabel('Principal Component')
    plt.title('Scree Plot')
    plt.show()
    pca_df = pd.DataFrame(pca_data, index=[*samples], columns=labels)
    plt.scatter(pca_df.PC1, pca_df.PC2)
    plt.title('My PCA Graph')
    plt.xlabel('PC1 - {0}%'.format(per_var[0]))
    plt.ylabel('PC2 - {0}%'.format(per_var[1]))
    for sample in pca_df.index:
        plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
    if prediction:
        plt.savefig("./images/prediction/img1.png")
    else:
        plt.savefig("./images/PCA+SVM/img1.png")
    plt.show()

    # # Determine which genes had the biggest influence on PC1
    # # get the name of the top 10 measurements (wavelength) that contribute most to pc1.
    # loading_scores = pd.Series(pca.components_[0], index=waves)
    # sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)
    # top_10_genes = sorted_loading_scores[0:10].index.values
    # print(loading_scores[top_10_genes])

    dataset = np.column_stack((tmp, pca_df.values[:,[0,1]]))
    # print(dataset)
    return dataset

# pca1('/Users/skye/PycharmProjects/20190302/data/光谱数据.xls')
# pca1('/Users/skye/PycharmProjects/20190302/data/测试(预测)数据集.csv')