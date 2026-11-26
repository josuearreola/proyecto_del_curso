import os
import base64
import subprocess

project_dir = r"c:\Users\josue\proyecto_del_curso"
screenshots_dir = os.path.join(project_dir, "docs", "screenshots")

def get_base64_img(filename):
    path = os.path.join(screenshots_dir, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            ext = os.path.splitext(filename)[1].lower()
            mime = "image/png" if ext == ".png" else "image/jpeg"
            return f"data:{mime};base64,{data}"
    return ""

img1 = get_base64_img("01_home_mobile.jpg")
img2 = get_base64_img("02_menu_mobile.jpg")
img3 = get_base64_img("03_home_desktop_install.jpg")
img4 = get_base64_img("04_service_worker_activo.jpg")
img5 = get_base64_img("05_indexeddb_posts.jpg")
img6 = get_base64_img("06_indexeddb_sync_posts.jpg")
img7 = get_base64_img("07_supabase_database.jpg")

# VS Code code images
code_vercel = get_base64_img("vscode_vercel.png")
code_manifest = get_base64_img("vscode_manifest.png")
code_sw = get_base64_img("vscode_sw_sync.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Caso de Estudio: Progressive Web App UTEQGram</title>
    <style>
        @page {{
            size: A4;
            margin: 16mm 18mm 16mm 18mm;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            color: #000000;
            line-height: 1.45;
            font-size: 13px;
            margin: 0;
            padding: 0;
        }}
        .page {{
            page-break-after: always;
            break-after: page;
        }}
        .page:last-child {{
            page-break-after: auto;
            break-after: auto;
        }}
        h1 {{
            font-size: 20px;
            color: #000000;
            margin-top: 0;
            margin-bottom: 12px;
            font-weight: bold;
        }}
        h2 {{
            font-size: 16px;
            color: #000000;
            margin-top: 0;
            margin-bottom: 10px;
            font-weight: bold;
        }}
        h3 {{
            font-size: 13.5px;
            color: #000000;
            margin-top: 12px;
            margin-bottom: 6px;
            font-weight: bold;
        }}
        h1, h2, h3 {{
            break-after: avoid;
            page-break-after: avoid;
        }}
        p {{
            margin-top: 0;
            margin-bottom: 8px;
            text-align: justify;
            color: #000000;
        }}
        ul, ol {{
            margin-top: 0;
            margin-bottom: 8px;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 3px;
            color: #000000;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 8px;
            margin-bottom: 12px;
            font-size: 12px;
            break-inside: avoid;
            page-break-inside: avoid;
        }}
        th, td {{
            border: 1px solid #444444;
            padding: 6px 8px;
            text-align: left;
            color: #000000;
        }}
        th {{
            font-weight: bold;
            color: #000000;
        }}
        .badge-success {{
            font-weight: bold;
            color: #000000;
        }}
        .meta-data {{
            margin-bottom: 16px;
        }}
        .meta-data p {{
            margin: 3px 0;
            font-size: 13px;
            color: #000000;
        }}
        a {{
            color: #000000;
            text-decoration: underline;
        }}
        /* VS Code Code Images */
        .vscode-container {{
            margin: 8px 0 10px 0;
            text-align: left;
            break-inside: avoid;
            page-break-inside: avoid;
        }}
        .vscode-img {{
            max-width: 100%;
            height: auto;
            display: block;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }}
        /* Evidence Images - Large, No Borders */
        .evidence-row {{
            display: flex;
            gap: 16px;
            justify-content: center;
            align-items: flex-start;
            margin: 10px 0;
            break-inside: avoid;
            page-break-inside: avoid;
        }}
        .evidence-col {{
            flex: 1;
            text-align: center;
        }}
        .evidence-item {{
            margin: 12px 0 16px 0;
            text-align: center;
            break-inside: avoid;
            page-break-inside: avoid;
        }}
        .evidence-img-large {{
            width: 96%;
            max-width: 650px;
            height: auto;
            max-height: 250px;
            object-fit: contain;
            display: block;
            margin: 0 auto 6px auto;
            border: none;
            background: transparent;
        }}
        .evidence-img-mobile {{
            max-width: 230px;
            height: auto;
            max-height: 340px;
            object-fit: contain;
            display: block;
            margin: 0 auto 6px auto;
            border: none;
            background: transparent;
        }}
        .evidence-caption {{
            font-size: 11.5px;
            color: #000000;
            text-align: center;
            margin-top: 4px;
        }}
    </style>
</head>
<body>

    <!-- PAGINA 1: Justificación de Plataformas y Herramientas -->
    <div class="page">
        <h1>Reporte de Caso de Estudio: Progressive Web App</h1>
        <div class="meta-data">
            <p><strong>Proyecto:</strong> UTEQGram (Aplicación Web Progresiva)</p>
            <p><strong>URL de Producción:</strong> <a href="https://proyectodelcurso.vercel.app">https://proyectodelcurso.vercel.app</a></p>
            <p><strong>Repositorio GitHub:</strong> <a href="https://github.com/josuearreola/proyecto_del_curso">https://github.com/josuearreola/proyecto_del_curso</a></p>
        </div>

        <h2>1. Justificación de Plataformas y Herramientas Utilizadas</h2>
        <p>
            Para la construcción y puesta en marcha del proyecto se seleccionaron herramientas estándar de la industria que garantizan rendimiento, mantenibilidad y nula dependencia de empaquetadores complejos:
        </p>
        <table>
            <thead>
                <tr>
                    <th style="width: 25%;">Plataforma / Herramienta</th>
                    <th style="width: 20%;">Categoría</th>
                    <th style="width: 55%;">Justificación Técnica</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>HTML5 / CSS3 / JavaScript (ES6)</strong></td>
                    <td>Frontend Base</td>
                    <td>Uso de tecnologías estándar nativas de la web para máxima velocidad de carga, compatibilidad multiplataforma y cero sobrecarga de frameworks externos.</td>
                </tr>
                <tr>
                    <td><strong>Material Design Lite (MDL)</strong></td>
                    <td>Diseño UI / UX</td>
                    <td>Proporciona una interfaz visual estructurada basada en los lineamientos Material Design de Google, con componentes adaptables a móviles (cajón de navegación, tarjetas, botones flotantes y snackbars).</td>
                </tr>
                <tr>
                    <td><strong>Service Worker API</strong></td>
                    <td>Arquitectura PWA</td>
                    <td>Componente central que se ejecuta en un hilo separado al navegador. Intercepta el tráfico de red HTTP, gestiona el almacenamiento en caché de los activos estáticos (App Shell) y habilita el procesamiento en segundo plano.</td>
                </tr>
                <tr>
                    <td><strong>IndexedDB (vía librería idb.js)</strong></td>
                    <td>Almacenamiento Local</td>
                    <td>Base de datos transaccional NoSQL integrada en el navegador. Supera las limitaciones de localStorage (5MB y síncrono), permitiendo persistir objetos JSON estructurados de gran tamaño de manera asíncrona.</td>
                </tr>
                <tr>
                    <td><strong>Background Sync API</strong></td>
                    <td>Sincronización Diferida</td>
                    <td>Permite delegar peticiones de red al Service Worker mediante el evento sync, garantizando que el usuario no pierda su información al crear publicaciones sin señal.</td>
                </tr>
                <tr>
                    <td><strong>Supabase (PostgreSQL & Storage)</strong></td>
                    <td>Backend as a Service</td>
                    <td>Proporciona una base de datos relacional robusta accesible directamente mediante API RESTful segura con cabeceras de autorización y servicio de almacenamiento en la nube para recursos multimedia.</td>
                </tr>
                <tr>
                    <td><strong>Vercel</strong></td>
                    <td>Hosting & Edge Network</td>
                    <td>Plataforma de despliegue en la nube que suministra certificados SSL automáticos (HTTPS mandatorio para Service Workers y WebAPKs), CDN global para distribución de activos estáticos y entrega de baja latencia.</td>
                </tr>
                <tr>
                    <td><strong>Git & GitHub</strong></td>
                    <td>Control de Versiones & CI/CD</td>
                    <td>Control de versiones distribuido que facilita la trazabilidad de cambios y se conecta de manera continua con Vercel para despliegues automatizados en cada actualización de la rama principal.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- PAGINA 2: Parámetros de Configuración (Parte 1: Vercel y Manifest) -->
    <div class="page">
        <h2>2. Parámetros de Configuración de las Plataformas</h2>

        <h3>2.1. Configuración de Despliegue en Vercel (vercel.json)</h3>
        <p>
            Para instruir a Vercel que sirva los activos estáticos y el Service Worker desde la raíz pública sin requerir pasos de compilación complejos, se implementó el archivo de configuración en la raíz del repositorio:
        </p>
        <div class="vscode-container">
            <img class="vscode-img" src="{code_vercel}" alt="Código vercel.json en Visual Studio Code" style="max-width: 480px;">
        </div>
        <ul>
            <li><strong>outputDirectory: "public":</strong> Indica a la red de Vercel que el directorio base de entrega es la carpeta <code>public/</code>, garantizando que el archivo <code>/sw.js</code> tenga alcance sobre la totalidad del origen <code>/</code>.</li>
            <li><strong>cleanUrls: true:</strong> Habilita el enrutamiento limpio de rutas amigables en el cliente sin requerir la extensión <code>.html</code>.</li>
        </ul>

        <h3>2.2. Manifiesto de la Aplicación Web (public/manifest.json)</h3>
        <p>
            Parámetro fundamental para cumplir con los criterios de instalabilidad de Google Chrome y la generación de WebAPKs en dispositivos Android:
        </p>
        <div class="vscode-container">
            <img class="vscode-img" src="{code_manifest}" alt="Código manifest.json en Visual Studio Code" style="max-width: 620px;">
        </div>
        <ul>
            <li><strong>name y short_name:</strong> Identificadores formal y abreviado de la aplicación en el sistema operativo.</li>
            <li><strong>display: "standalone":</strong> Oculta la barra de direcciones y elementos de navegación del navegador web, ejecutando la PWA con apariencia de app nativa.</li>
            <li><strong>icons:</strong> Matriz que define iconos de 192x192 y 512x512 píxeles, incluyendo la variante con propósito <code>maskable</code> requerida para la adaptación de iconos adaptativos en Android.</li>
        </ul>
    </div>

    <!-- PAGINA 3: Parámetros de Configuración (Parte 2: Service Worker y Supabase) -->
    <div class="page">
        <h3>2.3. Configuración del Service Worker y Estrategias de Caché (public/sw.js)</h3>
        <p>
            El Service Worker gestiona el almacenamiento en caché y la sincronización en segundo plano mediante un manejador robusto de promesas:
        </p>
        <ul>
            <li><strong>Control de versiones de caché:</strong> <code>CACHE_STATIC_NAME = 'static-v10'</code> y <code>CACHE_DYNAMIC_NAME = 'dynamic-v10'</code>. Garantizan la invalidación inmediata de recursos obsoletos en el evento <code>activate</code>.</li>
            <li><strong>Precaching (App Shell):</strong> En el evento <code>install</code> se precachean de manera atómica los archivos esenciales: <code>index.html</code>, <code>offline.html</code>, <code>manifest.json</code>, hojas de estilo CSS, librerías JavaScript e iconos.</li>
            <li><strong>Sincronización en segundo plano con Promise.all:</strong> El evento <code>sync</code> recorre el almacén <code>sync-posts</code> manteniendo vivo el hilo del Service Worker hasta confirmar la respuesta exitosa de Supabase:</li>
        </ul>
        <div class="vscode-container">
            <img class="vscode-img" src="{code_sw}" alt="Código sw.js en Visual Studio Code" style="max-width: 650px;">
        </div>

        <h3>2.4. Configuración de Base de Datos y API en Supabase</h3>
        <ul>
            <li><strong>Endpoint RESTful:</strong> <code>https://xmmkfhtidsgyrebpmcij.supabase.co/rest/v1/post</code></li>
            <li><strong>Esquema de Tabla post:</strong> Campos <code>id</code> (text, primary key), <code>title</code> (text), <code>location</code> (text), <code>image</code> (text).</li>
            <li><strong>Cabeceras de Petición HTTP:</strong> <code>apikey</code> y <code>Authorization: Bearer &lt;ANON_KEY&gt;</code> para acceso autenticado de lectura e inserción sin restricciones indebidas de CORS.</li>
        </ul>
    </div>

    <!-- PAGINA 4: Arquitectura de Pantallas, Vistas y Manejo de Datos -->
    <div class="page">
        <h2>3. Arquitectura de Pantallas, Vistas y Manejo de Datos</h2>

        <h3>3.1. Pantallas y Home</h3>
        <ul>
            <li><strong>Home / Feed Principal:</strong> Pantalla principal donde se renderiza la cabecera institucional, la imagen representativa del campus de la UTEQ, el botón flotante de publicación (+) y el contenedor dinámico de publicaciones.</li>
            <li><strong>Cajón Lateral de Navegación (Drawer):</strong> Menú colapsable adaptativo que permite desplazarse hacia el Feed, la pantalla de Ayuda y habilitar notificaciones push.</li>
            <li><strong>Modal de Creación de Publicación:</strong> Panel deslizante animado con inputs de Material Design para ingresar título y localización.</li>
            <li><strong>Pantalla de Respaldo Offline (offline.html):</strong> Vista de contingencia servida por el Service Worker ante fallos de red al solicitar páginas no cacheadas.</li>
        </ul>

        <h3>3.2. Vistas del Lado del Cliente (Client-Side Rendering - CSR)</h3>
        <p>
            La aplicación emplea renderizado dinámico en el cliente. El archivo JavaScript <code>feed.js</code> realiza la iteración de los registros (obtenidos de la API remota o de IndexedDB) y construye dinámicamente en el DOM los elementos correspondientes mediante <code>createCard(data)</code>, aplicando los estilos de Material Design sin requerir recargas completas ni renderizado en servidor (SSR).
        </p>

        <h3>3.3. Gestión de Datos: Locales, Remotos y Offline</h3>
        <table>
            <thead>
                <tr>
                    <th style="width: 20%;">Ámbito</th>
                    <th style="width: 30%;">Tecnología / Mecanismo</th>
                    <th style="width: 50%;">Comportamiento Implementado</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Remoto (Online)</strong></td>
                    <td>Supabase REST API (PostgreSQL)</td>
                    <td>Al estar conectado, la aplicación consulta <code>/rest/v1/post?select=*</code> para obtener las últimas publicaciones compartidas por la comunidad universitaria.</td>
                </tr>
                <tr>
                    <td><strong>Local (Caché de Lectura)</strong></td>
                    <td>IndexedDB (Almacén posts)</td>
                    <td>Cada respuesta exitosa de la red actualiza de inmediato el almacén <code>posts</code> en el dispositivo del usuario. Si el usuario vuelve a abrir la app sin conexión, los datos se cargan al instante desde IndexedDB.</td>
                </tr>
                <tr>
                    <td><strong>Offline (Cola de Escritura)</strong></td>
                    <td>IndexedDB (Almacén sync-posts) + SyncManager</td>
                    <td>Si el usuario crea un post sin internet, los datos se resguardan en <code>sync-posts</code> y se registra el evento <code>sync-new-posts</code>. En cuanto la conectividad regresa, el Service Worker procesa la cola y la envía a Supabase.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- PAGINA 5: Reporte de Pruebas -->
    <div class="page">
        <h2>4. Reporte de Pruebas</h2>
        <p>
            A continuación se detalla la matriz de casos de prueba ejecutados sobre el entorno de producción desplegado en Vercel, evaluando la experiencia tanto en dispositivos móviles como en equipos de escritorio:
        </p>

        <table>
            <thead>
                <tr>
                    <th style="width: 8%;">ID</th>
                    <th style="width: 25%;">Caso de Prueba</th>
                    <th style="width: 35%;">Procedimiento Realizado</th>
                    <th style="width: 22%;">Resultado Obtenido</th>
                    <th style="width: 10%;">Estado</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>CP-01</strong></td>
                    <td>Despliegue y entrega segura HTTPS</td>
                    <td>Ingreso a la URL <code>https://proyectodelcurso.vercel.app</code> desde navegador Edge y Chrome.</td>
                    <td>Carga instantánea bajo HTTPS con certificado SSL válido y activos servidos por CDN.</td>
                    <td><span class="badge-success">EXITOSO</span></td>
                </tr>
                <tr>
                    <td><strong>CP-02</strong></td>
                    <td>Registro y Ciclo de Vida del Service Worker</td>
                    <td>Apertura de DevTools -> Application -> Service Workers.</td>
                    <td>Service Worker <code>sw.js</code> registrado con estado activo y en ejecución (ID #748) con control del cliente.</td>
                    <td><span class="badge-success">EXITOSO</span></td>
                </tr>
                <tr>
                    <td><strong>CP-03</strong></td>
                    <td>Criterio de Instalabilidad PWA (Desktop)</td>
                    <td>Verificación del icono de instalación en la barra del navegador en escritorio.</td>
                    <td>El navegador muestra el botón "Instalar UTEQGram", permitiendo ejecutarla en ventana independiente sin barras de navegación.</td>
                    <td><span class="badge-success">EXITOSO</span></td>
                </tr>
                <tr>
                    <td><strong>CP-04</strong></td>
                    <td>Criterio de Instalabilidad PWA (Móvil)</td>
                    <td>Navegación en dispositivo móvil y selección de "Instalar aplicación".</td>
                    <td>Descarga e instalación en el cajón de aplicaciones con icono nativo y splash screen institucional.</td>
                    <td><span class="badge-success">EXITOSO</span></td>
                </tr>
                <tr>
                    <td><strong>CP-05</strong></td>
                    <td>Persistencia en Base de Datos Local IndexedDB</td>
                    <td>Inspección de DevTools -> IndexedDB -> <code>posts-store</code> -> <code>posts</code>.</td>
                    <td>Se confirman 8 registros descargados de la nube almacenados localmente para consulta offline inmediata.</td>
                    <td><span class="badge-success">EXITOSO</span></td>
                </tr>
                <tr>
                    <td><strong>CP-06</strong></td>
                    <td>Creación y Encolamiento Offline</td>
                    <td>Desconexión de red (modo avión / offline en DevTools) y envío de formulario de posteo.</td>
                    <td>La publicación se guarda en <code>sync-posts</code> dentro de IndexedDB con notificación visual al usuario.</td>
                    <td><span class="badge-success">EXITOSO</span></td>
                </tr>
                <tr>
                    <td><strong>CP-07</strong></td>
                    <td>Sincronización en Segundo Plano (Background Sync)</td>
                    <td>Reactivación del acceso a internet tras crear posts offline.</td>
                    <td>El evento <code>sync</code> procesa las solicitudes, confirma inserción en Supabase y limpia el almacén <code>sync-posts</code>.</td>
                    <td><span class="badge-success">EXITOSO</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- PAGINA 6: Evidencias - Dispositivos y Navegación (Figuras 1, 2, 3 Grandes y Sin Recuadro) -->
    <div class="page">
        <h2>5. Evidencias del Caso de Estudio</h2>
        <p>
            Capturas de pantalla recabadas durante la ejecución de las pruebas sobre la aplicación publicada en Vercel, evaluando la experiencia móvil y la instalabilidad en escritorio:
        </p>

        <div class="evidence-row">
            <div class="evidence-col">
                <img class="evidence-img-mobile" src="{img1}" alt="Vista Home Móvil">
                <div class="evidence-caption">Figura 1. Vista Home en dispositivo móvil (URL en producción y feed de publicaciones).</div>
            </div>
            <div class="evidence-col">
                <img class="evidence-img-mobile" src="{img2}" alt="Menú Lateral Móvil">
                <div class="evidence-caption">Figura 2. Menú de navegación lateral adaptativo (Drawer) con accesos directos.</div>
            </div>
        </div>

        <div class="evidence-item" style="margin-top: 14px;">
            <img class="evidence-img-large" src="{img3}" alt="Vista Desktop con Instalación PWA" style="max-height: 230px;">
            <div class="evidence-caption">Figura 3. Aplicación en escritorio mostrando el botón de instalación PWA en la barra de direcciones del navegador.</div>
        </div>
    </div>

    <!-- PAGINA 7: Evidencias - Service Worker y Persistencia Local (Figuras 4, 5, 6 Grandes y Sin Recuadro) -->
    <div class="page">
        <h3>5.2. Ciclo de Vida del Service Worker y Persistencia Local</h3>
        
        <div class="evidence-item">
            <img class="evidence-img-large" src="{img4}" alt="Service Worker Activo" style="max-height: 220px;">
            <div class="evidence-caption">Figura 4. Panel Application de DevTools: Service Worker registrado, activado y en ejecución (#748).</div>
        </div>

        <div class="evidence-item">
            <img class="evidence-img-large" src="{img5}" alt="IndexedDB Posts" style="max-height: 220px;">
            <div class="evidence-caption">Figura 5. Almacén IndexedDB 'posts': Persistencia de publicaciones remotas para consulta offline inmediata.</div>
        </div>

        <div class="evidence-item">
            <img class="evidence-img-large" src="{img6}" alt="IndexedDB Sync Posts" style="max-height: 200px;">
            <div class="evidence-caption">Figura 6. Almacén IndexedDB 'sync-posts': Cola de sincronización en segundo plano con registros diferidos.</div>
        </div>
    </div>

    <!-- PAGINA 8: Evidencias - Supabase y Conclusiones -->
    <div class="page">
        <h3>5.3. Persistencia Remota en Base de Datos Cloud (Supabase)</h3>

        <div class="evidence-item" style="margin-bottom: 24px;">
            <img class="evidence-img-large" src="{img7}" alt="Base de Datos Supabase" style="max-height: 320px; width: 100%;">
            <div class="evidence-caption">Figura 7. Panel de Supabase (Table Editor): Persistencia de registros en la tabla 'post' accesible vía API REST.</div>
        </div>

        <h2>6. Conclusiones</h2>
        <p>
            La implementación de <strong>UTEQGram</strong> demostró la efectividad de las Progressive Web Apps para entornos educativos con condiciones de red variables. Gracias a la combinación de Service Workers, IndexedDB y Background Sync, la aplicación brinda una experiencia de usuario idéntica a la de una aplicación nativa, eliminando la fricción de instalación por tiendas tradicionales y garantizando la integridad de los datos en todo momento.
        </p>
        <p>
            El despliegue automatizado en Vercel sobre HTTPS junto a la persistencia en la nube provista por Supabase proporciona una solución integral, escalable y mantenible para la comunidad de la UTEQ.
        </p>
    </div>

</body>
</html>
"""

html_path = os.path.join(project_dir, "documento_reporte.html")
pdf_path = os.path.join(project_dir, "Reporte_Caso_Estudio_PWA_UTEQGram.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generado exitosamente en: {html_path}")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
if os.path.exists(pdf_path):
    print(f"PDF generado exitosamente en: {pdf_path} (Tamano: {os.path.getsize(pdf_path)} bytes)")
else:
    print("Error generando PDF:", res.stderr)
