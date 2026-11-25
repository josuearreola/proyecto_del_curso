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
            return f"data:image/jpeg;base64,{data}"
    return ""

img1 = get_base64_img("01_home_mobile.jpg")
img2 = get_base64_img("02_menu_mobile.jpg")
img3 = get_base64_img("03_home_desktop_install.jpg")
img4 = get_base64_img("04_service_worker_activo.jpg")
img5 = get_base64_img("05_indexeddb_posts.jpg")
img6 = get_base64_img("06_indexeddb_sync_posts.jpg")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Caso de Estudio - Progressive Web App UTEQGram</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm 18mm 20mm 18mm;
            @bottom-right {{
                content: counter(page);
            }}
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            color: #222222;
            line-height: 1.5;
            font-size: 13px;
            margin: 0;
            padding: 0;
        }}
        h1 {{
            font-size: 24px;
            color: #1a237e;
            border-bottom: 2px solid #1a237e;
            padding-bottom: 8px;
            margin-top: 0;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        h2 {{
            font-size: 17px;
            color: #283593;
            border-bottom: 1px solid #c5cae9;
            padding-bottom: 4px;
            margin-top: 24px;
            margin-bottom: 10px;
        }}
        h3 {{
            font-size: 14px;
            color: #303f9f;
            margin-top: 16px;
            margin-bottom: 6px;
        }}
        p {{
            margin-top: 0;
            margin-bottom: 10px;
            text-align: justify;
        }}
        ul, ol {{
            margin-top: 0;
            margin-bottom: 10px;
            padding-left: 22px;
        }}
        li {{
            margin-bottom: 4px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            margin-bottom: 15px;
            font-size: 12px;
        }}
        th, td {{
            border: 1px solid #cccccc;
            padding: 7px 10px;
            text-align: left;
        }}
        th {{
            background-color: #f0f2f5;
            font-weight: bold;
            color: #1a237e;
        }}
        .badge-success {{
            color: #2e7d32;
            font-weight: bold;
        }}
        pre, code {{
            font-family: Consolas, "Courier New", monospace;
            background-color: #f5f5f5;
            font-size: 11px;
        }}
        pre {{
            border: 1px solid #e0e0e0;
            border-left: 3px solid #3f51b5;
            padding: 8px 12px;
            overflow-x: auto;
            margin-top: 6px;
            margin-bottom: 12px;
        }}
        .meta-box {{
            background-color: #f8f9fa;
            border: 1px solid #dcdcdc;
            padding: 12px 16px;
            margin-bottom: 20px;
            border-radius: 4px;
        }}
        .meta-box p {{
            margin: 4px 0;
            font-size: 13px;
        }}
        h1, h2, h3 {{
            page-break-after: avoid;
        }}
        table, tr, .evidence-card, pre, .meta-box {{
            page-break-inside: avoid;
        }}
        .evidence-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
            margin-top: 12px;
            margin-bottom: 12px;
        }}
        .evidence-card {{
            border: 1px solid #dcdcdc;
            padding: 8px;
            background: #fafafa;
            border-radius: 4px;
            page-break-inside: avoid;
            margin-bottom: 8px;
        }}
        .evidence-card img {{
            width: 100%;
            height: 220px;
            object-fit: contain;
            display: block;
            margin-bottom: 6px;
            background: #ffffff;
            border: 1px solid #eeeeee;
        }}
        .evidence-caption {{
            font-size: 11px;
            font-weight: bold;
            color: #333333;
            text-align: center;
        }}
    </style>
</head>
<body>

    <h1>Reporte de Caso de Estudio: Progressive Web App</h1>
    <div class="meta-box">
        <p><strong>Proyecto:</strong> UTEQGram (Aplicación Web Progresiva)</p>
        <p><strong>Caso de Estudio:</strong> Plataforma social y colaborativa estudiantil con soporte Offline-First</p>
        <p><strong>URL de Producción:</strong> <a href="https://proyectodelcurso.vercel.app">https://proyectodelcurso.vercel.app</a></p>
        <p><strong>Repositorio GitHub:</strong> <a href="https://github.com/josuearreola/proyecto_del_curso">https://github.com/josuearreola/proyecto_del_curso</a></p>
        <p><strong>Fecha de Emisión:</strong> Noviembre 2026</p>
    </div>

    <h2>1. Descripción del Caso de Estudio</h2>
    <p>
        El proyecto <strong>UTEQGram</strong> surge de la necesidad de ofrecer a los estudiantes y docentes de la Universidad Tecnológica de Querétaro (UTEQ) una plataforma ágil, liviana y confiable para compartir vivencias y actividades institucionales. El campus cuenta con áreas donde la conectividad a internet móvil es inestable o nula. 
    </p>
    <p>
        Para dar solución a este reto, se diseñó e implementó una <strong>Progressive Web App (PWA)</strong> bajo una filosofía <em>Offline-First</em>. Esta arquitectura permite a la aplicación seguir operando plenamente sin conexión: los usuarios pueden visualizar publicaciones previamente almacenadas, navegar por las pantallas del sistema y redactar nuevos aportes que se resguardan de forma segura en una cola transaccional local para sincronizarse de manera transparente en cuanto la red vuelve a estar disponible.
    </p>

    <h2>2. Justificación de Plataformas y Herramientas Utilizadas</h2>
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
                <td>Proporciona una interfaz visual profesional basada en los lineamientos Material Design de Google, con componentes adaptables a móviles (cajón de navegación, tarjetas, botones flotantes de acción y snackbars de notificación).</td>
            </tr>
            <tr>
                <td><strong>Service Worker API</strong></td>
                <td>Arquitectura PWA</td>
                <td>Componente central que se ejecuta en un hilo separado al navegador. Intercepta el tráfico de red HTTP, gestiona el almacenamiento en caché de los activos estáticos (App Shell) y habilita el procesamiento en segundo plano.</td>
            </tr>
            <tr>
                <td><strong>IndexedDB (vía librería <code>idb.js</code>)</strong></td>
                <td>Almacenamiento Local</td>
                <td>Base de datos transaccional NoSQL integrada en el navegador. Supera las limitaciones de <code>localStorage</code> (5MB y síncrono), permitiendo persistir objetos JSON estructurados de gran tamaño de manera asíncrona.</td>
            </tr>
            <tr>
                <td><strong>Background Sync API</strong></td>
                <td>Sincronización Diferida</td>
                <td>Permite delegar peticiones de red al Service Worker mediante el evento <code>sync</code>, garantizando que el usuario no pierda su información al crear publicaciones sin señal.</td>
            </tr>
            <tr>
                <td><strong>Supabase (PostgreSQL & Storage)</strong></td>
                <td>Backend as a Service (BaaS)</td>
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

    <div class="page-break"></div>

    <h2>3. Parámetros de Configuración de las Plataformas</h2>

    <h3>3.1. Configuración de Despliegue en Vercel (<code>vercel.json</code>)</h3>
    <p>
        Para instruir a Vercel que sirva los activos estáticos y el Service Worker desde la raíz pública sin requerir pasos de transpilación, se definió:
    </p>
    <pre>{{
  "outputDirectory": "public",
  "cleanUrls": true
}}</pre>
    <ul>
        <li><code>outputDirectory: "public"</code>: Indica a la red de Vercel que el directorio base de entrega es la carpeta <code>public/</code>, garantizando que <code>/sw.js</code> tenga alcance sobre la totalidad del origen <code>/</code>.</li>
        <li><code>cleanUrls: true</code>: Habilita el enrutamiento limpio de rutas amigables en el cliente.</li>
    </ul>

    <h3>3.2. Manifiesto de la Aplicación Web (<code>public/manifest.json</code>)</h3>
    <p>
        Parámetro fundamental para cumplir con los criterios de instalabilidad de Google Chrome y Android WebAPK:
    </p>
    <pre>{{
  "name": "UTEQGram",
  "short_name": "UTEQGram",
  "description": "App sencilla parecida a Instagram para compartir momentos",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "background_color": "#ffffff",
  "theme_color": "#3f51b5",
  "icons": [
    {{ "src": "/src/images/icons/icon-192x192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" }},
    {{ "src": "/src/images/icons/icon-512x512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" }},
    {{ "src": "/src/images/icons/icon-512x512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }}
  ]
}}</pre>

    <h3>3.3. Configuración del Service Worker y Estrategias de Caché (<code>public/sw.js</code>)</h3>
    <ul>
        <li><strong>Control de versiones de caché:</strong> <code>CACHE_STATIC_NAME = 'static-v10'</code> y <code>CACHE_DYNAMIC_NAME = 'dynamic-v10'</code>. Garantizan la invalidación inmediata de recursos obsoletos en el evento <code>activate</code>.</li>
        <li><strong>Precaching (App Shell):</strong> En el evento <code>install</code> se precachean de manera atómica los archivos esenciales: <code>index.html</code>, <code>offline.html</code>, <code>manifest.json</code>, hojas de estilo CSS, librerías JavaScript e iconos.</li>
        <li><strong>Sincronización en segundo plano con <code>Promise.all</code>:</strong> El evento <code>sync</code> recorre el almacén <code>sync-posts</code> manteniendo vivo el Service Worker hasta confirmar la respuesta exitosa de Supabase:
            <pre>self.addEventListener('sync', function (event) {{
  if (event.tag === 'sync-new-posts') {{
    event.waitUntil(
      readAllData('sync-posts').then(function (data) {{
        return Promise.all(data.map(function (post) {{
          return fetch(SUPABASE_URL + '/rest/v1/post', {{
            method: 'POST',
            headers: {{ 'apikey': SUPABASE_KEY, 'Authorization': 'Bearer ' + SUPABASE_KEY, 'Content-Type': 'application/json' }},
            body: JSON.stringify(post)
          }}).then(function (res) {{
            if (res.ok) return deleteItemFromData('sync-posts', post.id);
          }});
        }}));
      }})
    );
  }}
}});</pre>
        </li>
    </ul>

    <h3>3.4. Configuración de Base de Datos y API en Supabase</h3>
    <ul>
        <li><strong>Endpoint RESTful:</strong> <code>https://xmmkfhtidsgyrebpmcij.supabase.co/rest/v1/post</code></li>
        <li><strong>Esquema de Tabla <code>post</code>:</strong> Campos <code>id</code> (text, primary key), <code>title</code> (text), <code>location</code> (text), <code>image</code> (text).</li>
        <li><strong>Cabeceras de Petición HTTP:</strong> <code>apikey</code> y <code>Authorization: Bearer &lt;ANON_KEY&gt;</code> para acceso autenticado de lectura e inserción sin restricciones indebidas de CORS.</li>
    </ul>

    <div class="page-break"></div>

    <h2>4. Arquitectura de Pantallas, Vistas y Manejo de Datos</h2>

    <h3>4.1. Pantallas y Home</h3>
    <ul>
        <li><strong>Home / Feed Principal:</strong> Pantalla principal donde se renderiza la cabecera institucional, la imagen representativa del campus de la UTEQ, el botón flotante de publicación (+) y el contenedor dinámico de publicaciones.</li>
        <li><strong>Cajón Lateral de Navegación (Drawer):</strong> Menú colapsable adaptativo que permite desplazarse hacia el Feed, la pantalla de Ayuda y habilitar notificaciones push.</li>
        <li><strong>Modal de Creación de Publicación:</strong> Panel deslizante animado con inputs flotantes de Material Design para ingresar título y localización.</li>
        <li><strong>Pantalla de Respaldo Offline (<code>offline.html</code>):</strong> Vista de contingencia servida por el Service Worker ante fallos de red al solicitar páginas no cacheadas.</li>
    </ul>

    <h3>4.2. Vistas del Lado del Cliente (Client-Side Rendering - CSR)</h3>
    <p>
        La aplicación emplea renderizado dinámico en el cliente. El archivo JavaScript <code>feed.js</code> realiza la iteración de los registros (obtenidos de la API remota o de IndexedDB) y construye dinámicamente en el DOM los elementos correspondientes mediante <code>createCard(data)</code>, aplicando los estilos de Material Design sin requerir recargas completas ni renderizado en servidor (SSR).
    </p>

    <h3>4.3. Gestión de Datos: Locales, Remotos y Offline</h3>
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
                <td>IndexedDB (Almacén <code>posts</code>)</td>
                <td>Cada respuesta exitosa de la red actualiza de inmediato el almacén <code>posts</code> en el dispositivo del usuario. Si el usuario vuelve a abrir la app sin conexión, los datos se cargan al instante desde IndexedDB.</td>
            </tr>
            <tr>
                <td><strong>Offline (Cola de Escritura)</strong></td>
                <td>IndexedDB (Almacén <code>sync-posts</code>) + SyncManager</td>
                <td>Si el usuario crea un post sin internet, los datos se resguardan en <code>sync-posts</code> y se registra el evento <code>sync-new-posts</code>. En cuanto la conectividad regresa, el Service Worker procesa la cola y la envía a Supabase.</td>
            </tr>
        </tbody>
    </table>

    <h2>5. Reporte de Pruebas</h2>
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

    <div class="page-break"></div>

    <h2>6. Evidencias del Caso de Estudio</h2>
    <p>
        Capturas de pantalla recabadas durante la ejecución de las pruebas sobre la aplicación publicada en Vercel y ejecutada en entornos móviles y de escritorio:
    </p>

    <div class="evidence-grid">
        <div class="evidence-card">
            <img src="{img1}" alt="Vista Home Móvil">
            <div class="evidence-caption">Figura 1. Vista Home en dispositivo móvil (URL Vercel y tarjetas de publicaciones).</div>
        </div>
        <div class="evidence-card">
            <img src="{img2}" alt="Menú Lateral Móvil">
            <div class="evidence-caption">Figura 2. Menú de navegación lateral adaptativo (Drawer) con accesos a Feed y Ayuda.</div>
        </div>
        <div class="evidence-card">
            <img src="{img3}" alt="Vista Desktop con Instalación PWA">
            <div class="evidence-caption">Figura 3. Aplicación en escritorio mostrando el botón de instalación PWA en la barra de direcciones.</div>
        </div>
        <div class="evidence-card">
            <img src="{img4}" alt="Service Worker Activo">
            <div class="evidence-caption">Figura 4. Panel Application de DevTools: Service Worker activado y en ejecución (#748).</div>
        </div>
        <div class="evidence-card">
            <img src="{img5}" alt="IndexedDB Posts">
            <div class="evidence-caption">Figura 5. Almacén IndexedDB 'posts': Persistencia de publicaciones remotas para consulta offline.</div>
        </div>
        <div class="evidence-card">
            <img src="{img6}" alt="IndexedDB Sync Posts">
            <div class="evidence-caption">Figura 6. Almacén IndexedDB 'sync-posts': Cola de sincronización en segundo plano con registros pendientes.</div>
        </div>
    </div>

    <h2>7. Conclusiones</h2>
    <p>
        La implementación de <strong>UTEQGram</strong> demostró la efectividad de las Progressive Web Apps para entornos educativos con condiciones de red variables. Gracias a la combinación de Service Workers, IndexedDB y Background Sync, la aplicación brinda una experiencia de usuario idéntica a la de una aplicación nativa, eliminando la fricción de instalación por tiendas tradicionales y garantizando la integridad de los datos en todo momento.
    </p>

</body>
</html>
"""

html_path = os.path.join(project_dir, "documento_reporte.html")
pdf_path = os.path.join(project_dir, "Reporte_Caso_Estudio_PWA_UTEQGram.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generado exitosamente en: {html_path}")

# Run Edge headless to print to PDF
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
