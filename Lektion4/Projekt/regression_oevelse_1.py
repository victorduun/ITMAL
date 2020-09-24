def question_1a():
    from sklearn import datasets
    import matplotlib.pyplot as plt

    diabetes = datasets.load_diabetes()
    X = diabetes.data
    y = diabetes.target
    f = diabetes.feature_names

    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Feature X, y scatter plots', fontsize=16)

    for i in range(0, 2):
        for j in range(0, 2):
            axs[i, j].scatter(X[:, i * 2 + j], y)
            axs[i, j].set_title(f[i * 2 + j])

    plt.show()


question_1a()

#%% md
# Test

#%%