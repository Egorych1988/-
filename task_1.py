def check_round(num):
    return int(num * 100) / 100 == num


def calc_prices(input_price_with_nds, proc_nds):
    coefficient = 1 + proc_nds / 100.0
    up_price_with_nds = down_price_with_nds = int(input_price_with_nds * 100) / 100
    up_price_without_nds = down_price_without_nds = up_price_with_nds / coefficient

    while not check_round(up_price_without_nds) and not check_round(down_price_without_nds):
        if down_price_with_nds > 0.01:
            down_price_with_nds = round(down_price_with_nds - 0.01, 2)
            down_price_without_nds = down_price_with_nds / coefficient
        up_price_with_nds = round(up_price_with_nds + 0.01, 2)
        up_price_without_nds = up_price_with_nds / coefficient

    if check_round(up_price_without_nds):
        corrected_price_with_nds = up_price_with_nds
        corrected_price_without_nds = up_price_without_nds
    else:
        corrected_price_with_nds = down_price_with_nds
        corrected_price_without_nds = down_price_without_nds

    return round(corrected_price_with_nds, 2), round(corrected_price_without_nds, 2)


# Пример использования
if __name__ == "__main__":
    prices_1 = calc_prices(1.81, 20)
    print(f"CorrectedPriceWithNDS: {prices_1[0]},  CorrectedPriceWithoutNDS: {prices_1[1]}")
