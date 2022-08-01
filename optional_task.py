import pandas as pd


class ReaderCsv:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df_csv = pd.read_csv(csv_file, sep=';')

    def read_file(self):
        print(self.df_csv)

    def add_string(self, movie, note, rating):
        self.df_csv.loc[len(self.df_csv.index)] = [movie, note, rating]

    def delete_string(self, index):
        self.df_csv = self.df_csv.drop([index], axis=0)
        self.df_csv = self.df_csv.reset_index(drop=True)

    def show_max_rating(self):
        print('-- Get films with the highest rating --')
        return self.df_csv[self.df_csv.rating == self.df_csv.rating.max()]

    def show_min_rating(self):
        print('-- Get films with the lowest rating --')
        return self.df_csv[self.df_csv.rating == self.df_csv.rating.min()]

    def show_avg_rating(self):
        print('-- Get average rating among all films --')
        return self.df_csv.rating.mean()


example_string = {'movie': 'Disturbing the Peace',
                  'note': 'Former marshall Jim Dillon must pick up his gun again to battle a gang of outlaw bikers that have invaded his small-town of Horse Cave.',
                  'rating': 1}

if __name__ == '__main__':
    file_name = 'films.csv'

    file = ReaderCsv(file_name)
    # file.add_string(**example_string)
    file.read_file()
    # file.delete_string(5)
    # file.read_file()
    # print(file.show_max_rating(), '\n')
    # print(file.show_min_rating(), '\n')
    # print(file.show_avg_rating(), '\n')
