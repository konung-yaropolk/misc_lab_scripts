#!/usr/bin/env python3
# Settings block:

RESP_DURATION = 2
TO_DO_LIST = [

    ['Field_6_registered.tif',
     {
         'DIRECTORY': 'F: /Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_04_19/',
         'start': 22003,    # in ms
         'sampling_interval': 1,  # in s
         'epoch duration': 60,  # in s
         'n_epochs': 10,

     }
     ],

]


if __name__ == '__main__':
    import main
    main.main()
