import os
from playwright.sync_api import sync_playwright

output_dir = r"c:\Users\josue\proyecto_del_curso\docs\screenshots"
os.makedirs(output_dir, exist_ok=True)

html_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0;
    padding: 20px;
    background: transparent;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  }
  .vscode-window {
    background-color: #1e1e1e;
    border-radius: 6px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    overflow: hidden;
    width: fit-content;
    min-width: 580px;
    max-width: 780px;
    border: 1px solid #333333;
  }
  .vscode-header {
    background-color: #181818;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 35px;
    border-bottom: 1px solid #2b2b2b;
  }
  .tabs-container {
    display: flex;
    align-items: center;
    height: 100%;
  }
  .tab {
    background-color: #1e1e1e;
    color: #ffffff;
    padding: 0 14px;
    height: 100%;
    font-size: 12.5px;
    font-family: "Segoe UI", sans-serif;
    border-top: 1px solid #0078d4;
    display: flex;
    align-items: center;
    gap: 8px;
    border-right: 1px solid #252525;
  }
  .file-icon {
    font-size: 13px;
    color: #cbbe80;
    font-weight: bold;
  }
  .tab-close {
    font-size: 11px;
    color: #858585;
    margin-left: 6px;
    display: flex;
    align-items: center;
  }
  .win-controls {
    display: flex;
    align-items: center;
    height: 100%;
  }
  .win-btn {
    width: 44px;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .win-btn svg {
    display: block;
  }
  .editor {
    padding: 14px 18px;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 13px;
    line-height: 1.5;
    color: #d4d4d4;
  }
  .line {
    display: flex;
  }
  .ln {
    width: 32px;
    color: #858585;
    user-select: none;
    text-align: right;
    margin-right: 18px;
  }
  .code {
    white-space: pre;
  }
  .kwd { color: #569cd6; } /* keywords */
  .prop { color: #9cdcfe; } /* json props, obj properties */
  .str { color: #ce9178; } /* strings */
  .num { color: #b5cea8; } /* numbers, booleans */
  .fn { color: #dcdcaa; } /* functions */
  .com { color: #6a9955; font-style: italic; } /* comments */
</style>
</head>
<body>
  {content}
</body>
</html>
"""

win_buttons = """
    <div class="win-controls">
      <div class="win-btn">
        <svg width="10" height="1" viewBox="0 0 10 1"><path fill="#cccccc" d="M0 0h10v1H0z"/></svg>
      </div>
      <div class="win-btn">
        <svg width="10" height="10" viewBox="0 0 10 10"><path fill="none" stroke="#cccccc" stroke-width="1" d="M0.5 0.5h9v9h-9z"/></svg>
      </div>
      <div class="win-btn">
        <svg width="10" height="10" viewBox="0 0 10 10"><path fill="none" stroke="#cccccc" stroke-width="1.2" d="M0 0l10 10m0-10L0 10"/></svg>
      </div>
    </div>
"""

snippets = {
    "vscode_vercel.png": f"""
    <div class="vscode-window" id="target">
      <div class="vscode-header">
        <div class="tabs-container">
          <div class="tab">
            <span class="file-icon">{{}}</span>
            <span>vercel.json</span>
            <span class="tab-close">✕</span>
          </div>
        </div>
        {win_buttons}
      </div>
      <div class="editor">
        <div class="line"><span class="ln">1</span><span class="code">{{</span></div>
        <div class="line"><span class="ln">2</span><span class="code">  <span class="prop">"outputDirectory"</span>: <span class="str">"public"</span>,</span></div>
        <div class="line"><span class="ln">3</span><span class="code">  <span class="prop">"cleanUrls"</span>: <span class="num">true</span></span></div>
        <div class="line"><span class="ln">4</span><span class="code">}}</span></div>
      </div>
    </div>
    """,
    
    "vscode_manifest.png": f"""
    <div class="vscode-window" id="target">
      <div class="vscode-header">
        <div class="tabs-container">
          <div class="tab">
            <span class="file-icon">{{}}</span>
            <span>manifest.json</span>
            <span class="tab-close">✕</span>
          </div>
        </div>
        {win_buttons}
      </div>
      <div class="editor">
        <div class="line"><span class="ln">1</span><span class="code">{{</span></div>
        <div class="line"><span class="ln">2</span><span class="code">  <span class="prop">"name"</span>: <span class="str">"UTEQGram"</span>,</span></div>
        <div class="line"><span class="ln">3</span><span class="code">  <span class="prop">"short_name"</span>: <span class="str">"UTEQGram"</span>,</span></div>
        <div class="line"><span class="ln">4</span><span class="code">  <span class="prop">"description"</span>: <span class="str">"App sencilla parecida a Instagram para compartir momentos"</span>,</span></div>
        <div class="line"><span class="ln">5</span><span class="code">  <span class="prop">"start_url"</span>: <span class="str">"/"</span>,</span></div>
        <div class="line"><span class="ln">6</span><span class="code">  <span class="prop">"scope"</span>: <span class="str">"/"</span>,</span></div>
        <div class="line"><span class="ln">7</span><span class="code">  <span class="prop">"display"</span>: <span class="str">"standalone"</span>,</span></div>
        <div class="line"><span class="ln">8</span><span class="code">  <span class="prop">"orientation"</span>: <span class="str">"portrait-primary"</span>,</span></div>
        <div class="line"><span class="ln">9</span><span class="code">  <span class="prop">"background_color"</span>: <span class="str">"#ffffff"</span>,</span></div>
        <div class="line"><span class="ln">10</span><span class="code">  <span class="prop">"theme_color"</span>: <span class="str">"#3f51b5"</span>,</span></div>
        <div class="line"><span class="ln">11</span><span class="code">  <span class="prop">"icons"</span>: [</span></div>
        <div class="line"><span class="ln">12</span><span class="code">    {{ <span class="prop">"src"</span>: <span class="str">"/src/images/icons/icon-192x192.png"</span>, <span class="prop">"sizes"</span>: <span class="str">"192x192"</span>, <span class="prop">"type"</span>: <span class="str">"image/png"</span>, <span class="prop">"purpose"</span>: <span class="str">"any"</span> }},</span></div>
        <div class="line"><span class="ln">13</span><span class="code">    {{ <span class="prop">"src"</span>: <span class="str">"/src/images/icons/icon-512x512.png"</span>, <span class="prop">"sizes"</span>: <span class="str">"512x512"</span>, <span class="prop">"type"</span>: <span class="str">"image/png"</span>, <span class="prop">"purpose"</span>: <span class="str">"any"</span> }},</span></div>
        <div class="line"><span class="ln">14</span><span class="code">    {{ <span class="prop">"src"</span>: <span class="str">"/src/images/icons/icon-512x512-maskable.png"</span>, <span class="prop">"sizes"</span>: <span class="str">"512x512"</span>, <span class="prop">"type"</span>: <span class="str">"image/png"</span>, <span class="prop">"purpose"</span>: <span class="str">"maskable"</span> }}</span></div>
        <div class="line"><span class="ln">15</span><span class="code">  ]</span></div>
        <div class="line"><span class="ln">16</span><span class="code">}}</span></div>
      </div>
    </div>
    """,

    "vscode_sw_sync.png": f"""
    <div class="vscode-window" id="target">
      <div class="vscode-header">
        <div class="tabs-container">
          <div class="tab">
            <span class="file-icon" style="color:#f7df1e;">JS</span>
            <span>sw.js</span>
            <span class="tab-close">✕</span>
          </div>
        </div>
        {win_buttons}
      </div>
      <div class="editor">
        <div class="line"><span class="ln">119</span><span class="code"><span class="kwd">self</span>.<span class="fn">addEventListener</span>(<span class="str">'sync'</span>, <span class="kwd">function</span> (<span class="prop">event</span>) {{</span></div>
        <div class="line"><span class="ln">120</span><span class="code">    <span class="kwd">if</span> (<span class="prop">event</span>.<span class="prop">tag</span> === <span class="str">'sync-new-posts'</span>) {{</span></div>
        <div class="line"><span class="ln">121</span><span class="code">        <span class="prop">event</span>.<span class="fn">waitUntil</span>(</span></div>
        <div class="line"><span class="ln">122</span><span class="code">            <span class="fn">readAllData</span>(<span class="str">'sync-posts'</span>)</span></div>
        <div class="line"><span class="ln">123</span><span class="code">                .<span class="fn">then</span>(<span class="kwd">function</span> (<span class="prop">data</span>) {{</span></div>
        <div class="line"><span class="ln">124</span><span class="code">                    <span class="kwd">return</span> <span class="kwd">Promise</span>.<span class="fn">all</span>(<span class="prop">data</span>.<span class="fn">map</span>(<span class="kwd">function</span> (<span class="prop">post</span>) {{</span></div>
        <div class="line"><span class="ln">125</span><span class="code">                        <span class="kwd">return</span> <span class="fn">fetch</span>(<span class="prop">SUPABASE_URL</span> + <span class="str">'/rest/v1/post'</span>, {{</span></div>
        <div class="line"><span class="ln">126</span><span class="code">                            <span class="prop">method</span>: <span class="str">'POST'</span>,</span></div>
        <div class="line"><span class="ln">127</span><span class="code">                            <span class="prop">headers</span>: {{</span></div>
        <div class="line"><span class="ln">128</span><span class="code">                                <span class="str">'Content-Type'</span>: <span class="str">'application/json'</span>,</span></div>
        <div class="line"><span class="ln">129</span><span class="code">                                <span class="str">'apikey'</span>: <span class="prop">SUPABASE_KEY</span>,</span></div>
        <div class="line"><span class="ln">130</span><span class="code">                                <span class="str">'Authorization'</span>: <span class="str">'Bearer '</span> + <span class="prop">SUPABASE_KEY</span></span></div>
        <div class="line"><span class="ln">131</span><span class="code">                            }},</span></div>
        <div class="line"><span class="ln">132</span><span class="code">                            <span class="prop">body</span>: <span class="kwd">JSON</span>.<span class="fn">stringify</span>(<span class="prop">post</span>)</span></div>
        <div class="line"><span class="ln">133</span><span class="code">                        }})</span></div>
        <div class="line"><span class="ln">134</span><span class="code">                        .<span class="fn">then</span>(<span class="kwd">function</span> (<span class="prop">res</span>) {{</span></div>
        <div class="line"><span class="ln">135</span><span class="code">                            <span class="kwd">if</span> (<span class="prop">res</span>.<span class="prop">ok</span>) {{</span></div>
        <div class="line"><span class="ln">136</span><span class="code">                                <span class="kwd">return</span> <span class="fn">deleteItemFromData</span>(<span class="str">'sync-posts'</span>, <span class="prop">post</span>.<span class="prop">id</span>);</span></div>
        <div class="line"><span class="ln">137</span><span class="code">                            }}</span></div>
        <div class="line"><span class="ln">138</span><span class="code">                        }});</span></div>
        <div class="line"><span class="ln">139</span><span class="code">                    }}));</span></div>
        <div class="line"><span class="ln">140</span><span class="code">                }})</span></div>
        <div class="line"><span class="ln">141</span><span class="code">        );</span></div>
        <div class="line"><span class="ln">142</span><span class="code">    }}</span></div>
        <div class="line"><span class="ln">143</span><span class="code">}});</span></div>
      </div>
    </div>
    """
}

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        headless=True
    )
    page = browser.new_page(viewport={"width": 900, "height": 800}, device_scale_factor=2)
    
    for filename, snippet_html in snippets.items():
        full_html = html_template.replace("{content}", snippet_html)
        page.set_content(full_html)
        elem = page.locator("#target")
        out_path = os.path.join(output_dir, filename)
        elem.screenshot(path=out_path)
        print(f"Generated Windows VS Code: {out_path}")
        
    browser.close()

print("All Windows-style VS Code snippets generated successfully!")
