from django.shortcuts import render, redirect, get_object_or_404
from .models import Motor, Peminjaman
from .forms import PeminjamanForm


def home(request):
    search_query = request.GET.get('search', '')
    motors = Motor.objects.filter(nama__icontains=search_query)
    return render(request, 'home.html', {'motors': motors})

def about(request):
    return render(request, 'about.html')

def peminjaman(request):
    peminjamans = Peminjaman.objects.all() 
    return render(request, 'peminjaman.html', {'peminjamans': peminjamans})

def motor_detail(request, motor_id):
    motor = get_object_or_404(Motor, id=motor_id)

    if request.method == 'POST':
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            peminjaman = form.save(commit=False)
            peminjaman.motor = motor
            peminjaman.jumlah_bayar = motor.harga_per_hari * (peminjaman.tanggal_kembali - peminjaman.tanggal_pinjam).days

            if motor.stok > 0:
                motor.stok -= 1
                motor.save()

                peminjaman.save()

                return render(request, 'bukti_peminjaman.html', {'peminjaman': peminjaman, 'motor': motor})
            else:
                return render(request, 'detail.html', {'motor': motor, 'form': form, 'message': 'Stok motor habis, tidak dapat melakukan peminjaman.'})
    else:
        form = PeminjamanForm()
        

    return render(request, 'detail.html', {'motor': motor, 'form': form})

def update_sudah_bayar(request, peminjaman_id):
    peminjaman = get_object_or_404(Peminjaman, id=peminjaman_id)

    if peminjaman.sudah_bayar and peminjaman.status == 'Dipinjam':
        peminjaman.status = 'Dikembalikan'
        peminjaman.motor.stok += 1
        peminjaman.motor.save()
    elif not peminjaman.sudah_bayar:
        peminjaman.sudah_bayar = True
        peminjaman.status = 'Dipinjam'

    peminjaman.save()
    return redirect('peminjaman')