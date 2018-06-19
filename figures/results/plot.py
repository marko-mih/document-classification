# plot 1
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

def create_charts(features, eucl, cosine, tsss, name):
    plt.plot(features, eucl, color='r', label='Euclidean distance')
    plt.plot(features, cosine, color='g', label='Cosine similarity')
    fig = plt.plot(features, tsss, color='b', label='TS-SS')
    plt.ylim([0.,1.])
    plt.legend(fontsize=20) # using a size in points
    plt.legend(fontsize="x-large") # using a named size
    plt.xlabel('Feature dimensionality')
    plt.ylabel('Accuracy')
    plt.savefig(name)
    plt.clf()

if __name__ == '__main__':
    features = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 948 ]
    eucl = [ 0.588314125, 0.62369338, 0.651567944, 0.661216832, 0.661752881, 0.660948807, 0.660948807, 0.657464487, 0.656124363, 0.649959796, 0.648351648 ]
    cosine = [ 0.593406593, 0.6271777, 0.659608684, 0.673545966, 0.679442509, 0.686143125, 0.68239078, 0.682122755, 0.683462879, 0.683462879, 0.683998928 ]
    tsss = [ 0.585901903, 0.577325114, 0.600375235, 0.570892522, 0.547306352, 0.536585366, 0.531760922, 0.527204503, 0.52184401, 0.513267221, 0.512463147 ]
    create_charts(features, eucl, cosine, tsss, 'n_0_d_r.png')

    features = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 948 ]
    eucl = [ 0.593674618, 0.624229429, 0.65880461, 0.673545966, 0.679174484, 0.686143125, 0.68239078, 0.682122755, 0.683194854, 0.683462879, 0.683730903 ]
    cosine = [0.592870544, 0.627445725, 0.659608684, 0.673545966, 0.679442509, 0.686143125, 0.68239078, 0.682122755, 0.683462879, 0.683462879, 0.683998928, ]
    tsss = [ 0.592870544, 0.627445725, 0.659608684, 0.673545966, 0.679442509, 0.686143125, 0.68239078, 0.682122755, 0.683462879, 0.683462879, 0.683998928 ]
    create_charts(features, eucl, cosine, tsss, 'n_1_d_r.png')

    features = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, ]
    eucl = [ 0.219729156, 0.310939989, 0.3637812, 0.400690388, 0.413568773, 0.414099841, 0.418215613, 0.418481147, 0.41622411, 0.406399363, 0.403478492, 0.403876792, 0.399495486, 0.396574615, 0.395379713, 0.389537971, 0.39298991 ]
    cosine = [0.228226235, 0.344131705, 0.434545937, 0.501593202, 0.539431758, 0.562134891, 0.577801381, 0.590148699, 0.599973447, 0.608868826, 0.616436537, 0.625862985, 0.635687732, 0.639139671, 0.639405204, 0.639139671, 0.640600106, ]
    tsss = [ 0.214020181, 0.223446628, 0.175916091, 0.140467339, 0.114976102, 0.106744557, 0.102230483, 0.112187998, 0.105947955, 0.099309612, 0.095326606, 0.09559214, 0.092936803, 0.10236325, 0.100637281, 0.097185343, 0.117100372 ]
    create_charts(features, eucl, cosine, tsss, 'n_0_d_n.png')

    features = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 948 ]
    eucl = [ 0.228093468, 0.344264472, 0.434678704, 0.501593202, 0.539431758, 0.562134891, 0.577801381, 0.590148699, 0.599973447, 0.608868826, 0.615772703 ]
    cosine = [0.228226235, 0.344264472, 0.434545937, 0.501593202, 0.539431758, 0.562134891, 0.577801381, 0.590148699, 0.599973447, 0.608868826, 0.615772703 ]
    tsss = [ 0.228226235, 0.344264472, 0.434545937, 0.501593202, 0.539431758, 0.562134891, 0.577801381, 0.590148699, 0.599973447, 0.608868826, 0.615772703 ]
    create_charts(features, eucl, cosine, tsss, 'n_1_d_n.png')
