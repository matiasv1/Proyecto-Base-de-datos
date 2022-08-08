<?php
   /* Este archivo debe usarse para comprobar si existe una sesión válida 
   Considerar qué pasa cuando la sesión es válida/inválida para cada página:
   - Página principal
   - Mi perfil
   - Mi billetera
   - Administración de usuarios y todo el CRUD
   - Iniciar Sesión
   - Registrarse
   */
   session_start();
   if (isset($_SESSION["email"])){
      if ($_SESSION["id_rol"]==1) {
         echo // si inicia sesion un admin
               '<ul class="navbar-nav">
                  <!-- Visible solo si hay una sesión iniciada -->
                  <li class="nav-item">
                     <a class="nav-link" href="/user/profile.html"><image class="icon" src="/icon/profile.png" width="22"></image>Perfil</a>
                  </li>                  
                  <!-- Solo el admin puede revisar los usuarios -->
                  <li class="nav-item">
                     <a class="nav-link" href="/admin/users/all.html"><image class="icon" src="/icon/users.png" width="22"></image>Usuarios</a>
                  </li>
                  <li class="nav-item">
                     <a class="nav-link" href="/simulacion/simulacion.html"><image class="icon" src="/icon/simulacion.png" width="22"></image>Simulación</a>
                  </li>
               </ul>

               <ul class="navbar-nav ml-auto">
                     <!-- Visible solo si hay una sesión iniciada -->
                     <li class="nav-item">
                     <a href="#" class="nav-link" onclick="preguntarCierreSesion()">Cerrar Sesión</a>
                     </li>
               </ul>';
      }
      elseif ($_SESSION["id_rol"]==2) {
         echo // si inicia sesion un usuario comun
            '<ul class="navbar-nav">
                  <!-- Visible solo si hay una sesión iniciada -->
                  <li class="nav-item">
                     <a class="nav-link" href="/user/profile.html"><image class="icon" src="/icon/profile.png" width="23"></image>Perfil</a>
                  </li>
                  <!-- Solo los usuarios tienen billetera -->
                  <li class="nav-item">
                     <a class="nav-link" href="/user/wallet.html"><image class="icon" src="/icon/wallet.png" width="23"></image>Billetera</a>
                  </li>
                  <li class="nav-item">
                     <a class="nav-link" href="/simulacion/simulacion.html"><image class="icon" src="/icon/simulacion.png" width="22"></image>Simulación</a>
                  </li>
               </ul>

               <ul class="navbar-nav ml-auto">
               <!-- Visible solo si hay una sesión iniciada -->
                     <!-- Visible solo si hay una sesión iniciada -->
                     <li class="nav-item">
                     <a href="#" class="nav-link" onclick="preguntarCierreSesion()">Cerrar Sesión</a>
                     </li>
               </ul>';
      }
   }
   else { 
      echo // Si la session no esta iniciada (login / sign-up)
         '<ul class="navbar-nav ml-auto">
            <!-- Visible solo si NO hay una sesión iniciada -->
            <li class="nav-item">
               <a class="nav-link" href="/sesion/log-in.html">Iniciar Sesión</a>
            </li>
            <!-- Visible solo si NO hay una sesión iniciada -->
            <li class="nav-item">
               <a class="nav-link" href="/sesion/sign-up.html">Registrarse</a>
            </li>
         </ul>';
   }
?>