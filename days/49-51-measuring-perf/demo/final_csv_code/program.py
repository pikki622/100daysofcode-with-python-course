import cProfile

profiler = cProfile.Profile()
profiler.disable()

import research


def main():
    print("Weather research for Seattle, 2014-2015")
    print()
    profiler.enable()

    research.init()

    hot_days = research.hot_days()
    cold_days = research.cold_days()
    wet_days = research.wet_days()

    profiler.disable()

    print("The hottest 5 days:")
    for idx, d in enumerate(hot_days[:5]):
        print(f"{idx + 1}. {d.actual_max_temp} F on {d.date}")
    print()
    print("The coldest 5 days:")

    for idx, d in enumerate(cold_days[:5]):
        print(f"{idx + 1}. {d.actual_min_temp} F on {d.date}")
    print()
    print("The wettest 5 days:")

    for idx, d in enumerate(wet_days[:5]):
        print(f"{idx + 1}. {d.actual_precipitation} inches of rain on {d.date}")


if __name__ == '__main__':
    for _ in range(1, 100):
        main()

    profiler.print_stats(sort='cumtime')
