import classes as c
import settings as s


def main():

    for item in s.TO_DO_LIST:

        try:
            Parser = c.MetadataParser()
            movie_duration, start = Parser.Parse(
                s.PATH_PREFIX + item[0][:-len(s.INPUT_NAME_SUFFIX)])

            # if item[1]['start']:
            #     start = float(item[1]['start'])
            #     del item[1]['start']
            print(' ')
            der = c.Derivatives(item[0],
                                start,
                                movie_duration,
                                **item[1])
            der.process_secuence()

        except Exception as e:
            print(e)
            pass

    merger = c.TifColorMerger(s.PATH_PREFIX,
                              s.RED_NAME_ENDING,
                              s.GRN_NAME_ENDING,
                              s.BLE_NAME_ENDING,
                              s.OUTPUT_NAME_ENDING)

    merger.process_directory()


if __name__ == '__main__':
    main()
