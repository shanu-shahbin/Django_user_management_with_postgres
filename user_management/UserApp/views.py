from django.shortcuts import render, redirect  
from django.db import connection  


def view_users(request):  
    with connection.cursor() as cursor:  
        cursor.execute("SELECT * FROM users")  
        users = cursor.fetchall()  
    return render(request, 'view_users.html', {'users': users})  

 
def add_user(request):  
    if request.method == 'POST':  
        username = request.POST['username']  
        email = request.POST['email']  
        password = request.POST['password']  
        with connection.cursor() as cursor:  
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",   
                           [username, email, password])  
        return redirect('view_users')  
    return render(request, 'add_user.html')  


def update_user(request, user_id):  
    if request.method == 'POST':  
        username = request.POST['username']  
        email = request.POST['email']  
        password = request.POST['password']  
        with connection.cursor() as cursor:  
            cursor.execute("UPDATE users SET username=%s, email=%s, password=%s WHERE id=%s",   
                           [username, email, password, user_id])  
        return redirect('view_users')  
    with connection.cursor() as cursor:  
        cursor.execute("SELECT * FROM users WHERE id=%s", [user_id])  
        user = cursor.fetchone()  
    return render(request, 'update_user.html', {'user': user})  

 
def delete_user(request, user_id):  
    with connection.cursor() as cursor:  
        cursor.execute("DELETE FROM users WHERE id=%s", [user_id])  
    return redirect('view_users')  
