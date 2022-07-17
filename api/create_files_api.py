from xlsxwriter.utility import xl_col_to_name
from api.vfd_api import series_power_list, get_supplier, get_series, get_vfd_by_params, get_price_vfd
from utils.myexcel.myxls import Xlsx


class ComparisonZone:
    def __init__(self):
        self.suppliers = None


class Block:
    def __init__(self, series):
        self.series = series
        self.price_col = []


def column_by_n(n):
    return 6 * (n + 1)


def create_compare_price():
    comparison_zone = ComparisonZone()
    comparison_zone.suppliers = [3, 4, 5]
    comparison_zone.blocks = [
        Block((9, 11, 13)),
        Block((9, None, 14)),
        Block((7, 11, 13)),
        Block((7, None, 14)),
        Block((7, 12, 15)),
        Block((6, 12, 15)),
        Block((8, 12, 15)),
    ]

    eur_rub = 65.09

    xlsx = Xlsx('upload/compare.xlsx', overwrite=True)
    row = 1

    for i, supplier_id in enumerate(comparison_zone.suppliers):
        supplier = get_supplier(supplier_id)
        xlsx.ws.cell(row=row, column=column_by_n(i)).value = supplier.name

    row += 1

    for i, block in enumerate(comparison_zone.blocks):
        power_list = []
        for series_id in block.series:
            if series_id:
                power_list += series_power_list(series_id)
        power_list = set(power_list)
        power_list = sorted(power_list, key=lambda x: (x[1], x[0]))

        print(f'block{i + 1} power_list:')
        for x in power_list:
            print(x)
        print()

        row_p = row + 1
        for power in power_list:
            xlsx.ws.cell(row=row_p, column=1).value = power[0]
            xlsx.ws.cell(row=row_p, column=2).value = power[1]
            row_p += 1

        for j, series_id in enumerate(block.series):
            if series_id:
                series = get_series(series_id)
                xlsx.ws.cell(row=row, column=column_by_n(j)).value = f'{series.brand} {series.name}'

                supplier = get_supplier(comparison_zone.suppliers[j])
                currency = supplier.currency
                xlsx.ws.cell(row=row, column=column_by_n(j) + 2).value = currency

                if currency == 'RUB':
                    block.price_col.append(column_by_n(j) + 3)
                else:
                    block.price_col.append(column_by_n(j) + 2)

                row_s = row + 1
                for power in power_list:
                    power, voltage = power[0], power[1]
                    vfd = get_vfd_by_params(series, power, voltage)
                    if vfd:
                        xlsx.ws.cell(row=row_s, column=column_by_n(j)).value = vfd.article
                        xlsx.ws.cell(row=row_s, column=column_by_n(j) + 1).value = vfd.name

                        price = get_price_vfd(supplier, vfd)
                        col_r = None
                        if price:
                            price = price.price
                            price_val = price
                            if currency == 'RUB':
                                price_val = round(price_val / eur_rub, 2)
                            xlsx.ws.cell(row=row_s, column=column_by_n(j) + 2).value = price
                            col = xl_col_to_name(column_by_n(j) + 1)
                            xlsx.ws[f'{col}{row_s}'].number_format = '0.00'

                            col_r = column_by_n(j) + 2
                            if price != price_val:
                                col1 = xl_col_to_name(column_by_n(j) + 1)
                                col2 = xl_col_to_name(column_by_n(j) + 2)
                                xlsx.ws.cell(row=row_s, column=column_by_n(j) + 3).value = f'={col1}{row_s}/{eur_rub}'
                                xlsx.ws[f'{col2}{row_s}'].number_format = '0.00'
                                col_r = column_by_n(j) + 3

                        if j != 0:
                            col1 = xl_col_to_name(col_r - 1)
                            col2 = xl_col_to_name(block.price_col[0] - 1)
                            col = xl_col_to_name(col_r)
                            val_col2 = xlsx.ws[f'{col2}{row_s}'].value
                            if val_col2:
                                xlsx.ws.cell(row=row_s, column=col_r + 1).value = f'={col1}{row_s}/{col2}{row_s} - 1'
                                xlsx.ws[f'{col}{row_s}'].number_format = '0%'

                    row_s += 1

        row = row + len(power_list) + 2

    xlsx.width_auto() \
        .save_and_open()
