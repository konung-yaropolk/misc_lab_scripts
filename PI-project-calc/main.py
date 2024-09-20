import classes as c
import settings as s


def main():

    for item in s.TO_DO_LIST:
        der = c.Derivatives(item[0], **item[1])
        der.calculate_single_response()
        der.save(item[0] + '_DERIVATIVES.tif')


if __name__ == '__main__':
    main()
