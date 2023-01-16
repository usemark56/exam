from tkinter import *
root = Tk()
root.title('Конвертор довжин: Категорія')
root['bg']='#5cd1a0'
root.geometry("250x300")
def k():
    k = Toplevel(root)
    k.title('Конвертор довжин: Кілометри')
    k.geometry("250x300")
    k['bg'] = '#5cd1a0'
    def kmm():
        kmm = Toplevel(k)
        kmm.title('Конвертор довжин: Кілометри -> Метри')
        kmm.geometry("250x300")
        kmm['bg'] = '#5cd1a0'
        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 1000
            text.insert(END, b)
            entry.delete(0, END)
        label = Label(kmm, text='Введіть к-сть кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(kmm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(kmm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(kmm, text='Кількість метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(kmm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def kmdts():
        kmdts = Toplevel(k)
        kmdts.title('Конвертор довжин: Кілометри -> Дециметри')
        kmdts.geometry("250x300")
        kmdts['bg'] = '#5cd1a0'
        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 10000
            text.insert(END, b)
            entry.delete(0, END)
        label = Label(kmdts, text='Введіть к-сть кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(kmdts, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(kmdts, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(kmdts, text='Кількість дециметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(kmdts, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def kms():
        kms = Toplevel(k)
        kms.title('Конвертор довжин: Кілометри -> Сантиметри')
        kms.geometry("250x300")
        kms['bg'] = '#5cd1a0'
        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 100000
            text.insert(END, b)
            entry.delete(0, END)
        label = Label(kms, text='Введіть к-сть кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(kms, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(kms, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(kms, text='Кількість сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(kms, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def kmmm():
        kmmm = Toplevel(k)
        kmmm.title('Конвертор довжин: Кілометри -> Міліметри')
        kmmm.geometry("250x300")
        kmmm['bg'] = '#5cd1a0'
        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 1000000
            text.insert(END, b)
            entry.delete(0, END)
        label = Label(kmmm, text='Введіть к-сть кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(kmmm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(kmmm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(kmmm, text='Кількість міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(kmmm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    label = Label(k, text='Виберіть конвертор', fg='#77d9b0', bg='#0d4a31')
    label.pack()
    km_m = Button(k, text='Кілометри -> Метри', command=kmm, fg='#77d9b0', bg='#0d4a31')
    km_m.pack()
    km_dts = Button(k, text='Кілометри -> Дециметри', command=kmdts, fg='#77d9b0', bg='#0d4a31')
    km_dts.pack()
    km_s = Button(k, text='Кілометри -> Сантиметри', command=kms, fg='#77d9b0', bg='#0d4a31')
    km_s.pack()
    km_mm = Button(k, text='Кілометри -> Міліметри', command=kmmm, fg='#77d9b0', bg='#0d4a31')
    km_mm.pack()
def m():
    m = Toplevel(root)
    m.title('Конвертор довжин: Метри')
    m.geometry("250x300")
    m['bg'] = '#5cd1a0'
    def mkm():
        mkm = Toplevel(m)
        mkm.title('Конвертор довжин: Метри -> Кілометри')
        mkm.geometry("250x300")
        mkm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 1000
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(mkm, text='Введіть к-сть метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(mkm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(mkm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(mkm, text='Кількість кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(mkm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def mdts():
        mdts = Toplevel(m)
        mdts.title('Конвертор довжин: Метри -> Дециметри')
        mdts.geometry("250x300")
        mdts['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 10
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(mdts, text='Введіть к-сть метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(mdts, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(mdts, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(mdts, text='Кількість децеметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(mdts, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def ms():
        ms = Toplevel(m)
        ms.title('Конвертор довжин: Метри -> Сантиметри')
        ms.geometry("250x300")
        ms['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 100
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(ms, text='Введіть к-сть метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(ms, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(ms, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(ms, text='Кількість сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(ms, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def mmm():
        mmm = Toplevel(m)
        mmm.title('Конвертор довжин: Метри -> Міліметри')
        mmm.geometry("250x300")
        mmm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 1000
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(mmm, text='Введіть к-сть метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(mmm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(mmm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(mmm, text='Кількість міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(mmm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    label = Label(m, text='Виберіть конвертор', fg='#77d9b0', bg='#0d4a31')
    label.pack()
    m_km = Button(m, text='Метри -> Кілометри', command=mkm, fg='#77d9b0', bg='#0d4a31')
    m_km.pack()
    m_dts = Button(m, text='Метри -> Дециметри', command=mdts, fg='#77d9b0', bg='#0d4a31')
    m_dts.pack()
    m_s = Button(m, text='Метри -> Сантиметри', command=ms, fg='#77d9b0', bg='#0d4a31')
    m_s.pack()
    m_mm = Button(m, text='Метри -> Міліметри', command=mmm, fg='#77d9b0', bg='#0d4a31')
    m_mm.pack()
def d():
    d = Toplevel(root)
    d.title('Конвертор довжин: Дециметри')
    d.geometry("250x300")
    d['bg'] = '#5cd1a0'

    def dtskm():
        dtskm = Toplevel(d)
        dtskm.title('Конвертор довжин: Дециметри -> Кілометри')
        dtskm.geometry("250x300")
        dtskm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 10000
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(dtskm, text='Введіть к-сть дециметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(dtskm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(dtskm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(dtskm, text='Кількість кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(dtskm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def dtsm():
        dtsm = Toplevel(d)
        dtsm.title('Конвертор довжин: Дециметри -> Метри')
        dtsm.geometry("250x300")
        dtsm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 10
            text.insert(END, b)
            entry.delete(0, END)
        label = Label(dtsm, text='Введіть к-сть дециметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(dtsm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(dtsm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(dtsm, text='Кількість метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(dtsm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def dtss():
        dtss = Toplevel(d)
        dtss.title('Конвертор довжин: Дециметри -> Сантиметри')
        dtss.geometry("250x300")
        dtss['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 10
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(dtss, text='Введіть к-сть дециметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(dtss, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(dtss, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(dtss, text='Кількість сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(dtss, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def dtsmm():
        dtsmm = Toplevel(d)
        dtsmm.title('Конвертор довжин: Дециметри -> Міліметри')
        dtsmm.geometry("250x300")
        dtsmm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 100
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(dtsmm, text='Введіть к-сть дециметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(dtsmm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(dtsmm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(dtsmm, text='Кількість міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(dtsmm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    label = Label(d, text='Виберіть конвертор', fg='#77d9b0', bg='#0d4a31')
    label.pack()
    dts_km = Button(d, text='Дециметри -> Кілометри', command=dtskm, fg='#77d9b0', bg='#0d4a31')
    dts_km.pack()
    dts_m = Button(d, text='Дециметри -> Метри', command=dtsm, fg='#77d9b0', bg='#0d4a31')
    dts_m.pack()
    dts_s = Button(d, text='Дециметри -> Сантиметри', command=dtss, fg='#77d9b0', bg='#0d4a31')
    dts_s.pack()
    dts_mm = Button(d, text='Дециметри -> Міліметри', command=dtsmm, fg='#77d9b0', bg='#0d4a31')
    dts_mm.pack()
def s():
    s = Toplevel(root)
    s.title('Конвертор довжин: Сантиметри')
    s.geometry("250x300")
    s['bg'] = '#5cd1a0'
    def skm():
        skm = Toplevel(s)
        skm.title('Конвертор довжин: Сантиметри -> Кілометри')
        skm.geometry("250x300")
        skm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 100000
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(skm, text='Введіть к-сть сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(skm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(skm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(skm, text='Кількість кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(skm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def sm():
        sm = Toplevel(s)
        sm.title('Конвертор довжин: Сантиметри -> Метри')
        sm.geometry("250x300")
        sm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 100
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(sm, text='Введіть к-сть сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(sm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(sm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(sm, text='Кількість метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(sm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def sdts():
        sdts = Toplevel(s)
        sdts.title('Конвертор довжин: Сантиметри -> Дециметри')
        sdts.geometry("250x300")
        sdts['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 10
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(sdts, text='Введіть к-сть сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(sdts, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(sdts, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(sdts, text='Кількість дециметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(sdts, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def smm():
        smm = Toplevel(s)
        smm.title('Конвертор довжин: Сантиметри -> Міліметри')
        smm.geometry("250x300")
        smm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a * 10
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(smm, text='Введіть к-сть сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(smm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(smm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(smm, text='Кількість міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(smm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    label = Label(s, text='Виберіть конвертор', fg='#77d9b0', bg='#0d4a31')
    label.pack()
    s_km = Button(s, text='Сантиметри -> Кілометри', command=skm, fg='#77d9b0', bg='#0d4a31')
    s_km.pack()
    s_m = Button(s, text='Сантиметри -> Метри', command=sm, fg='#77d9b0', bg='#0d4a31')
    s_m.pack()
    s_dts = Button(s, text='Сантиметри -> Дециметри', command=sdts, fg='#77d9b0', bg='#0d4a31')
    s_dts.pack()
    s_mm = Button(s, text='Сантиметри -> Міліметри', command=smm, fg='#77d9b0', bg='#0d4a31')
    s_mm.pack()
def mm():
    mm = Toplevel(root)
    mm.title('Конвертор довжин: Міліметри')
    mm.geometry("250x300")
    mm['bg'] = '#5cd1a0'

    def mmkm():
        mmkm = Toplevel(mm)
        mmkm.title('Конвертор довжин: Міліметри -> Кілометри')
        mmkm.geometry("250x300")
        mmkm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 1000000
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(mmkm, text='Введіть к-сть міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(mmkm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(mmkm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(mmkm, text='Кількість кілометрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(mmkm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def mmm():
        mmm = Toplevel(mm)
        mmm.title('Конвертор довжин: Міліметри -> Метри')
        mmm.geometry("250x300")
        mmm['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 1000
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(mmm, text='Введіть к-сть міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(mmm, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(mmm, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(mmm, text='Кількість метрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(mmm, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def mmdts():
        mmdts = Toplevel(mm)
        mmdts.title('Конвертор довжин: Міліметри -> Дециметри')
        mmdts.geometry("250x300")
        mmdts['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 100
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(mmdts, text='Введіть к-сть міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(mmdts, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(mmdts, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(mmdts, text='Кількість дециметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(mmdts, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()
    def mms():
        mms = Toplevel(mm)
        mms.title('Конвертор довжин: Міліметри -> Сантиметри')
        mms.geometry("250x300")
        mms['bg'] = '#5cd1a0'

        def okok():
            text.delete(1.0, END)
            a = float(entry.get())
            b = a / 10
            text.insert(END, b)
            entry.delete(0, END)

        label = Label(mms, text='Введіть к-сть міліметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        entry = Entry(mms, bg='#29805b', font='Helvetica 20 italic', fg='White')
        entry.pack()
        ok = Button(mms, text='OK', command=okok, fg='#77d9b0', bg='#0d4a31')
        ok.pack()
        label = Label(mms, text='Кількість сантиметрів', fg='#77d9b0', bg='#0d4a31')
        label.pack()
        text = Text(mms, height=12, width=30, font='Futura 15', bg='#3eab7d')
        text.pack()

    label = Label(mm, text='Виберіть конвертор', fg='#77d9b0', bg='#0d4a31')
    label.pack()
    mm_km = Button(mm, text='Міліметри -> Кілометри', command=mmkm, fg='#77d9b0', bg='#0d4a31')
    mm_km.pack()
    mm_m = Button(mm, text='Міліметри -> Метри', command=mmm, fg='#77d9b0', bg='#0d4a31')
    mm_m.pack()
    mm_dts = Button(mm, text='Міліметри -> Дециметри', command=mmdts, fg='#77d9b0', bg='#0d4a31')
    mm_dts.pack()
    mm_s = Button(mm, text='Міліметри -> Сантиметри', command=mms, fg='#77d9b0', bg='#0d4a31')
    mm_s.pack()
label = Label(text='Виберіть категорію', fg='#77d9b0', bg='#0d4a31')
label.pack()
km = Button(text='Кілометри', command=k, fg='#77d9b0', bg='#0d4a31')
km.pack()
m = Button(text='Метри', command=m, fg='#77d9b0', bg='#0d4a31')
m.pack()
dts = Button(text='Дециметри', command=d, fg='#77d9b0', bg='#0d4a31')
dts.pack()
s = Button(text='Сантиметри', command=s, fg='#77d9b0', bg='#0d4a31')
s.pack()
mm = Button(text='Міліметри', command=mm, fg='#77d9b0', bg='#0d4a31')
mm.pack()
root.mainloop()