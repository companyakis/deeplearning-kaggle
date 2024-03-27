df.plot(figsize = (10, 7),
        xlim = [0, 30],
        ylim = [0, 1],
        grid = True,
        xlabel = "# of Epochs",
        style = ["b--", "b--*", "r-", "r--."]
        )

plt.title("Model Metrics")

plt.show()
