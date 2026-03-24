import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    print("Gráfico generado correctamente")

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('bar.png')
    plt.close()