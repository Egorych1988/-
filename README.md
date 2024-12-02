Входные параметры процедуры:
1. Внешняя система рассчитывает и передает нам рекомендованную цену с НДС - InputPriceWithNDS,
содержащую до 20 знаков после зарпятой
2. Процент НДС  -  ProcNDS : 0..99


ЗАДАЧА 1: Процедура должна рассчитать значение цен с НДС и без НДС (CorrectedPriceWithNDS,
CorrectedPriceWithoutNDS) так, чтобы CorrectedPriceWithNDS была предельно близко
к InputPriceWithNDS: |CorrectedPriceWithNDS-InputPriceWithNDS| -> min ...  и при этом
CorrectedPriceWithNDS и CorrectedPriceWithoutNDS содержали максимум 2 знака после
запятой и не требовали округлений. Обратите внимание не требовали округлений. 

ЗАДАЧА 2: Сделать интерфейс для проверки корректности вашего решения. 
