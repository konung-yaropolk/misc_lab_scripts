import classes as c
import settings as s


def main():

    for item in s.TO_DO_LIST:

        try:
            der = c.Derivatives(item[0], **item[1])
            der.process_secuence()
        except Exception as e:
            print(e)
            pass

    # Example usage
    creator = c.TifColorMerger(s.PATH_PREFIX,
                               s.RED_NAME_ENDING,
                               s.GRN_NAME_ENDING,
                               s.BLE_NAME_ENDING,
                               s.OUTPUT_NAME_ENDING)

    creator.process_directory()


if __name__ == '__main__':
    main()
