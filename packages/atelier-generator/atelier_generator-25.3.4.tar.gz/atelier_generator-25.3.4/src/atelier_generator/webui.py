import gradio as gr
from datetime import datetime
from gradio_modal import Modal

def AtelierWebUI(client, host: str = None, port: int = None, browser: bool = False, upload_size: str = "4MB",
                 public: bool = False, limit: int = 10, quiet: bool = False):
    """ 
    Start Atelier Generator Web UI with all features.
    
    Parameters:
    - client (Client): Atelier Generator instance
    - host (str): Server host
    - port (int): Server port
    - browser (bool): Launch browser automatically
    - upload_size (str): Maximum file size for uploads
    - public (bool): Enable public URL mode
    - limit (int): Maximum number of concurrent requests
    """
    try:
        ime_size         = client.list_atr_size
        ime_remix_model  = client.list_atr_remix_model
        ime_controlnets  = client.list_atr_controlnets
        ime_lora         = client.list_atr_lora_rt
        atr_models       = client.list_atr_models
        atr_models_guide = client.list_atr_models_guide
        atr_models_svi   = client.list_atr_models_svi
        atr_lora_svi     = client.list_atr_lora_svi
        atr_lora_flux    = client.list_atr_lora_flux
        atr_size         = client.list_atr_size
        atr_g_variation  = client.list_atr_g_variation
        atr_g_structure  = client.list_atr_g_structure
        atr_g_facial     = client.list_atr_g_facial
        atr_g_style      = client.list_atr_g_style
        sty_styles       = client.list_atr_styles

        system_theme = gr.themes.Default(
            primary_hue=gr.themes.colors.rose,
            secondary_hue=gr.themes.colors.rose,
            neutral_hue=gr.themes.colors.zinc
        )

        css = '''
        ::-webkit-scrollbar {
            display: none;
        }

        ::-webkit-scrollbar-button {
            display: none;
        }

        body {
            background-color: #000000;
            background-image: linear-gradient(45deg, #111111 25%, #000000 25%, #000000 50%, #111111 50%, #111111 75%, #000000 75%, #000000 100%);
            background-size: 40px 40px;
            -ms-overflow-style: none;
        }

        gradio-app {
            --body-background-fill: None;
        }
        footer {
            display: none !important;
        }

        .app.svelte-182fdeq.svelte-182fdeq {
            padding: 0px;
        }

        .grid-wrap.svelte-hpz95u.svelte-hpz95u {
            overflow-y: auto;
        }


        .image-frame.svelte-rrgd5g img {
            object-fit: contain;
        }

        .image-container.svelte-1l6wqyv {
            height: 100%;
        }

        .grid-container.svelte-eynlr2.svelte-eynlr2 {
            grid-template-rows: repeat(auto-fit, minmax(200px, 1fr));
            grid-template-columns: repeat(auto-fit, minmax(200px, 0.505fr));
        }

        .wrap.svelte-1sbaaot {
            align-items: inherit;
        }

        .wrap.svelte-z7cif2.svelte-z7cif2 {
            z-index: 100;
            max-height: 100%;
        }

        .stage-wrap.svelte-1sbaaot {
            transform: translate(0px, 266px);
        }

        button.svelte-1uw5tnk {
            margin-bottom: 8px;
            width: 192px;
            padding: 8px;
            border-radius: var(--container-radius);
        }

        .selected.svelte-1uw5tnk {
            background: var(--button-cancel-background-fill);
            color: var(--button-cancel-text-color);
            border-radius: 10px;
            border: none;
            position: relative;
            overflow: hidden;
        }

        .tab-nav.svelte-1uw5tnk {
            justify-content: space-evenly;
            border: 0px;
        }

        div.svelte-19hvt5v {
            border-radius: 10px;
            margin-top: 12px;
            border: 1px solid var(--border-color-primary);
        }

        input[type=range].svelte-pc1gm4 {
            background-image: linear-gradient(var(--color-accent), var(--color-accent));
        }

        .thumbnails.svelte-eynlr2.svelte-eynlr2 {
            align-items: center;
            gap: 10px;
            padding-left: 10px;
            padding-right: 10px;
        }

        .icon.svelte-1oiin9d {
            display: none;
        }

        .caption-label.svelte-eynlr2.svelte-eynlr2 {
            display: none;
        }

        input[type=number].svelte-pjtc3.svelte-pjtc3 {
            line-height: 0px;
        }
        
        /* Touch device optimizations */
        @media (hover: none) {
            button, input, select {
                min-height: 44px;
            }
        }

        /* Prevent zoom on input focus for iOS */
        @media screen and (-webkit-min-device-pixel-ratio: 0) { 
            select,
            textarea,
            input {
                font-size: 16px;
            }
        }
        '''

        def Markdown(name:str):
            return gr.Markdown(f"{name}")

        def Textbox(name:str, lines:int=1, max_lines:int=4):
            return gr.Textbox(placeholder=f"{name}", lines=lines, max_lines=max_lines, container=False)

        def Slider(min:int, max:int, step:float, value:int, label:str=None):
            return gr.Number(value=value, minimum=min, maximum=max, step=step, label=label)

        def Dropdown(choices:list, value:str, label:str=None):
            return gr.Dropdown(choices=choices, value=value, label=label, container=False if label is None else True)

        def Checkbox(name:str, value:bool):
            return gr.Checkbox(value=value, label=name, min_width=96)

        def Button(name:str, variant:str='secondary'):
            return gr.Button(name, variant=variant, min_width=96)

        def Number(name:str, value:int, min:int, step:float=0.01):
            return gr.Number(value=value, minimum=min, step=step, label=name)

        def Image(name:str, sources:list, height:int):
            return gr.Image(type="filepath", height=height, sources=sources, label=name)

        def Gallery(height:int):
            return gr.Gallery(height=height, object_fit="contain", container=False, show_share_button=False)

        def State(name:list):
            return gr.State(name)

        def ImageMask():
            return gr.ImageMask(
                            height="80%",
                            type="pil",
                            layers=False,
                            container=False,
                            transforms=[],
                            sources=["upload"],
                            brush=gr.Brush(default_size=24, colors=["#ffffff"], color_mode="fixed"),
                            eraser=gr.Eraser(default_size=24),
                        )

        def Paint():
            return gr.ImageEditor(
                            height="80%",
                            type="pil",
                            container=False,
                            transforms=['crop'],
                            sources=['upload', 'webcam', 'clipboard'],
                            crop_size='1:1',
                            brush=gr.Brush(default_size=24, color_mode="defaults"),
                            eraser=gr.Eraser(default_size=24),
                            layers=False
                        )
        
        def truncate_prompt(prompt, max_length=50):
            if prompt is None or prompt == "":
                return "No Prompt"
            return (prompt[:max_length] + '...') if len(prompt) > max_length else prompt        
        
        js_func = """
        function refresh() {
            const url = new URL(window.location);
            url.searchParams.set('__theme', url.searchParams.get('__theme') === 'dark' || !url.searchParams.get('__theme') ? 'light' : 'dark');
            window.location.href = url.href;
        }
        """
                
        with gr.Blocks(title=f"Atelier Generator", css=css, analytics_enabled=False, theme=system_theme, fill_height=True).queue(default_concurrency_limit=limit) as demo:
            
            with gr.Row():
                with gr.Column(scale=1):
                    Markdown(f"## <br><center>Atelier Generator Web UI")
                    Markdown(f"<center>Copyright (C) {datetime.now().year} Ikmal Said. All rights reserved")
                
                # with gr.Column(scale=0):
                #     ToggleDM = Button("Toggle Dark Mode")
                #     ToggleDM.click(fn=None, inputs=None, outputs=None, js=js_func)

            with gr.Tab("Image Generator"):
                
                def igen_prep(igen_pro, igen_neg, igen_mod, igen_siz, igen_svi, igen_flux, igen_sed, igen_sty, igen_enh, igen_ram):
                    caption = f"{truncate_prompt(igen_pro)} | Model: {igen_mod} | Size: {igen_siz} | Style: {igen_sty} | SVI LoRA: {igen_svi} | Flux LoRA: {igen_flux} | Seed: {igen_sed}"
                    results = client.image_generate(igen_pro, igen_neg, igen_mod, igen_siz, igen_svi, igen_flux, igen_sed, igen_sty, igen_enh)
                    if results is not None:
                        igen_ram.insert(0, (results, caption))
                    return igen_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Generator")
                        Markdown("<center>Basic Settings")
                        igen_pro = Textbox("Prompt for image...")
                        igen_neg = Textbox("Negative prompt...")
                        
                        Markdown("<center>Advanced Settings")
                        with gr.Row():
                            igen_mod = Dropdown(atr_models, atr_models[0], label="Model Selection")
                            igen_siz = Dropdown(atr_size, atr_size[0], label="Image Size")
                        with gr.Row():
                            igen_svi = Dropdown(atr_lora_svi, atr_lora_svi[0], label="SVI LoRA")
                            igen_flux = Dropdown(atr_lora_flux, atr_lora_flux[0], label="Flux LoRA")
                        
                        igen_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)

                        Markdown("<center>Style Presets")
                        igen_sty = Dropdown(sty_styles, sty_styles[0])
                        igen_enh = Checkbox("Enhance Prompt", False)
                        
                        with gr.Row():
                            igen_sub = Button("Generate", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        igen_res = Gallery(885.938)
                        igen_ram = State([])
                        igen_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=igen_prep,
                            inputs=[igen_pro, igen_neg, igen_mod, igen_siz, igen_svi, igen_flux, igen_sed, igen_sty, igen_enh, igen_ram],
                            outputs=[igen_res]
                        )    

            with gr.Tab("Transparent Generator"):
                
                def itra_prep(itra_pro, itra_neg, itra_siz, itra_sed, itra_sty, itra_enh, itra_ram):
                    caption = f"{truncate_prompt(itra_pro)} | Size: {itra_siz} | Style: {itra_sty}"
                    results = client.image_transparent(itra_pro, itra_neg, itra_siz, itra_sed, itra_sty, itra_enh)
                    if results is not None:
                        itra_ram.insert(0, (results, caption))
                    return itra_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Transparent Generator")
                        Markdown("<center>Basic Settings")
                        itra_pro = Textbox("Prompt for image...")
                        itra_neg = Textbox("Negative prompt...")
                        
                        Markdown("<center>Advanced Settings")
                        with gr.Row():
                            itra_siz = Dropdown(ime_size, ime_size[0], label="Image Size")
                        
                        itra_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)
                        
                        Markdown("<center>Style Presets")
                        itra_sty = Dropdown(sty_styles, sty_styles[0])
                        itra_enh = Checkbox("Enhance Prompt", False)
                        itra_sub = Button("Generate", "stop")

                    with gr.Column(variant="panel", scale=3) as result:
                        itra_res = Gallery(885.938)
                        itra_ram = State([])
                        itra_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=itra_prep,
                            inputs=[itra_pro, itra_neg, itra_siz, itra_sed, itra_sty, itra_enh, itra_ram],
                            outputs=[itra_res]
                        )

            with gr.Tab("Image Variation"):
                def ivar_prep(ivar_img, ivar_pro, ivar_neg, ivar_mod, ivar_siz, ivar_gst, ivar_svi, ivar_flux, ivar_sed, ivar_sty, ivar_enh, ivar_ram):
                    caption = f"{truncate_prompt(ivar_pro)} | Model: {ivar_mod} | Size: {ivar_siz} | Style: {ivar_sty}"
                    results = client.image_variation(ivar_img, ivar_pro, ivar_neg, ivar_mod, ivar_siz, 
                                            ivar_gst, ivar_svi, ivar_flux, ivar_sed, ivar_sty, ivar_enh)
                    if results is not None:
                        ivar_ram.insert(0, (results, caption))
                    return ivar_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Variation")
                        Markdown("<center>Basic Settings")
                        ivar_img = Image("Upload Image", ["upload"], 150)
                        ivar_pro = Textbox("Prompt for image...")
                        ivar_neg = Textbox("Negative prompt...")

                        Markdown("<center>Advanced Settings")
                        with gr.Group():
                            with gr.Row():
                                ivar_mod = Dropdown(atr_models_guide, atr_models_guide[0], label="Model Selection")
                                ivar_siz = Dropdown(atr_size, atr_size[0], label="Image Size")
                            ivar_gst = Dropdown(atr_g_variation, atr_g_variation[0], label="Guide Strength")
                            with gr.Row():
                                ivar_svi = Dropdown(atr_lora_svi, atr_lora_svi[0], label="SVI LoRA")
                                ivar_flux = Dropdown(atr_lora_flux, atr_lora_flux[0], label="Flux LoRA")
                        
                        ivar_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)

                        Markdown("<center>Style Presets")
                        ivar_sty = Dropdown(sty_styles, sty_styles[0])
                        ivar_enh = Checkbox("Enhance Prompt", False)
                        ivar_sub = Button("Generate", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        ivar_res = Gallery(961.344)
                        ivar_ram = State([])
                        ivar_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=ivar_prep,
                            inputs=[ivar_img, ivar_pro, ivar_neg, ivar_mod, ivar_siz, ivar_gst, ivar_svi, ivar_flux, ivar_sed, ivar_sty, ivar_enh, ivar_ram],
                            outputs=[ivar_res]
                        )

            with gr.Tab("Image Structure"):
                def istr_prep(istr_img, istr_pro, istr_neg, istr_mod, istr_siz, istr_gst, istr_svi, istr_sed, istr_sty, istr_enh, istr_ram):
                    caption = f"{truncate_prompt(istr_pro)} | Model: {istr_mod} | Size: {istr_siz} | Style: {istr_sty}"
                    results = client.image_structure(istr_img, istr_pro, istr_neg, istr_mod, istr_siz,
                                            istr_gst, istr_svi, istr_sed, istr_sty, istr_enh)
                    if results is not None:
                        istr_ram.insert(0, (results, caption))
                    return istr_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Structure")
                        Markdown("<center>Basic Settings")
                        istr_img = Image("Upload Image", ["upload"], 150)
                        istr_pro = Textbox("Prompt for image...")
                        istr_neg = Textbox("Negative prompt...")

                        Markdown("<center>Advanced Settings")
                        with gr.Group():
                            with gr.Row():
                                istr_mod = Dropdown(atr_models_svi, atr_models_svi[0], label="Model Selection")
                                istr_siz = Dropdown(atr_size, atr_size[0], label="Image Size")
                            with gr.Row():
                                istr_gst = Dropdown(atr_g_structure, atr_g_structure[0], label="Guide Strength")
                                istr_svi = Dropdown(atr_lora_svi, atr_lora_svi[0], label="SVI LoRA")
                        
                        istr_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)

                        Markdown("<center>Style Presets")
                        istr_sty = Dropdown(sty_styles, sty_styles[0])
                        istr_enh = Checkbox("Enhance Prompt", False)
                        istr_sub = Button("Generate", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        istr_res = Gallery(961.344)
                        istr_ram = State([])
                        istr_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=istr_prep,
                            inputs=[istr_img, istr_pro, istr_neg, istr_mod, istr_siz, istr_gst, istr_svi, istr_sed, istr_sty, istr_enh, istr_ram],
                            outputs=[istr_res]
                        )

            with gr.Tab("Image Facial"):
                def ifac_prep(ifac_img, ifac_pro, ifac_neg, ifac_mod, ifac_siz, ifac_gst, ifac_svi, ifac_sed, ifac_sty, ifac_enh, ifac_ram):
                    caption = f"{truncate_prompt(ifac_pro)} | Model: {ifac_mod} | Size: {ifac_siz} | Style: {ifac_sty}"
                    results = client.image_facial(ifac_img, ifac_pro, ifac_neg, ifac_mod, ifac_siz,
                                        ifac_gst, ifac_svi, ifac_sed, ifac_sty, ifac_enh)
                    if results is not None:
                        ifac_ram.insert(0, (results, caption))
                    return ifac_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Facial")
                        Markdown("<center>Basic Settings")
                        ifac_img = Image("Upload Image", ["upload"], 150)
                        ifac_pro = Textbox("Prompt for image...")
                        ifac_neg = Textbox("Negative prompt...")

                        Markdown("<center>Advanced Settings")
                        with gr.Group():
                            with gr.Row():
                                ifac_mod = Dropdown(atr_models_svi, atr_models_svi[0], label="Model Selection")
                                ifac_siz = Dropdown(atr_size, atr_size[0], label="Image Size")
                            with gr.Row():
                                ifac_gst = Dropdown(atr_g_facial, atr_g_facial[0], label="Guide Strength")
                                ifac_svi = Dropdown(atr_lora_svi, atr_lora_svi[0], label="SVI LoRA")
                        
                        ifac_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)

                        Markdown("<center>Style Presets")
                        ifac_sty = Dropdown(sty_styles, sty_styles[0])
                        ifac_enh = Checkbox("Enhance Prompt", False)
                        ifac_sub = Button("Generate", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        ifac_res = Gallery(961.344)
                        ifac_ram = State([])
                        ifac_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=ifac_prep,
                            inputs=[ifac_img, ifac_pro, ifac_neg, ifac_mod, ifac_siz, ifac_gst, ifac_svi, ifac_sed, ifac_sty, ifac_enh, ifac_ram],
                            outputs=[ifac_res]
                        )

            with gr.Tab("Image Style"):
                def isty_prep(isty_img, isty_pro, isty_neg, isty_mod, isty_siz, isty_gst, isty_svi, isty_sed, isty_sty, isty_enh, isty_ram):
                    caption = f"{truncate_prompt(isty_pro)} | Model: {isty_mod} | Size: {isty_siz} | Style: {isty_sty}"
                    results = client.image_style(isty_img, isty_pro, isty_neg, isty_mod, isty_siz,
                                        isty_gst, isty_svi, isty_sed, isty_sty, isty_enh)
                    if results is not None:
                        isty_ram.insert(0, (results, caption))
                    return isty_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Style")
                        Markdown("<center>Basic Settings")
                        isty_img = Image("Upload Image", ["upload"], 150)
                        isty_pro = Textbox("Prompt for image...")
                        isty_neg = Textbox("Negative prompt...")

                        Markdown("<center>Advanced Settings")
                        with gr.Group():
                            with gr.Row():
                                isty_mod = Dropdown(atr_models_svi, atr_models_svi[0], label="Model Selection")
                                isty_siz = Dropdown(atr_size, atr_size[0], label="Image Size")
                            with gr.Row():
                                isty_gst = Dropdown(atr_g_style, atr_g_style[0], label="Guide Strength")
                                isty_svi = Dropdown(atr_lora_svi, atr_lora_svi[0], label="SVI LoRA")
                        
                        isty_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)

                        Markdown("<center>Style Presets")
                        isty_sty = Dropdown(sty_styles, sty_styles[0])
                        isty_enh = Checkbox("Enhance Prompt", False)
                        isty_sub = Button("Generate", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        isty_res = Gallery(961.344)
                        isty_ram = State([])
                        isty_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=isty_prep,
                            inputs=[isty_img, isty_pro, isty_neg, isty_mod, isty_siz, isty_gst, isty_svi, isty_sed, isty_sty, isty_enh, isty_ram],
                            outputs=[isty_res]
                        )

            with gr.Tab("Image Controlnet"):
                
                def icn_prep(icn_img, icn_pro, icn_neg, icn_mod, icn_con, icn_str, icn_sca, icn_sed, icn_sty, icn_ram):
                    caption = f"{truncate_prompt(icn_pro)} | Model: {icn_mod} | Control: {icn_con} | Style: {icn_sty}"
                    results = client.image_controlnet(icn_img, icn_pro, icn_neg, icn_mod, icn_con, icn_str, icn_sca, icn_sed, icn_sty)
                    if results is not None:
                        icn_ram.insert(0, (results, caption))
                    return icn_ram

                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Controlnet")
                        Markdown("<center>Basic Settings")
                        icn_img = Image("Upload Image", ["upload"], 199)
                        icn_pro = Textbox("Prompt for image...")
                        icn_neg = Textbox("Negative prompt...")
                    
                        Markdown("<center>Advanced Settings")
                        with gr.Row():
                            icn_mod = Dropdown(ime_remix_model, ime_remix_model[0], label="Model Selection")
                            icn_con = Dropdown(ime_controlnets, ime_controlnets[0], label="Control Type")
                        with gr.Row():
                            icn_str = Slider(0, 100, 1, 70, "Controlnet Strength")
                            icn_sca = Slider(3, 15, 0.5, 9, "Prompt Scale")
                            
                        icn_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)
                        
                        Markdown("<center>Style Presets")
                        icn_sty = Dropdown(sty_styles, sty_styles[0])
                        icn_sub = Button("Generate", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        icn_res = Gallery(898.344)
                        icn_ram = State([])
                        
                        icn_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=icn_prep,
                            inputs=[icn_img, icn_pro, icn_neg, icn_mod, icn_con, icn_str, icn_sca, icn_sed, icn_sty, icn_ram],
                            outputs=[icn_res]
                        )    
                        
            with gr.Tab("Image Toolkit"):
                
                def usc_prep(itk_img, itk_ram):
                    caption = "Upscaled Image"
                    results = client.image_upscale(itk_img)
                    if results is not None:
                        itk_ram.insert(0, (results, caption))
                    return itk_ram
                
                def cfm_prep(itk_img, itk_ram):
                    caption = "Restored Image"
                    results = client.face_codeformer(itk_img)
                    if results is not None:
                        itk_ram.insert(0, (results, caption))
                    return itk_ram
                
                def bgr_prep(itk_img, itk_ram):
                    caption = "Background Removed"
                    results = client.image_bgremove(itk_img)
                    if results is not None:
                        itk_ram.insert(0, (results, caption))
                    return itk_ram

                def arc_prep(itk_img, arc_typ, itk_ram):
                    caption = f"Face Restored | Model: {arc_typ}"
                    results = client.face_gfpgan(itk_img, arc_typ)
                    if results is not None:
                        itk_ram.insert(0, (results, caption))
                    return itk_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Toolkit")
                        itk_img = Image("Upload Image", ["upload"], 199)
                        
                        Markdown("<center>Face Restoration")
                        arc_typ = Dropdown(client.list_atr_gfpgan, client.list_atr_gfpgan[0], label="Model Selection")
                        arc_sub = Button("Restore Face", "stop")
                        
                        Markdown("<center>Available Tools")
                        bgr_sub = Button("Remove Background")
                        usc_sub = Button("Upscale Image")
                        cfm_sub = Button("Restore Image")
                        cap_sub = Button("Caption Image")
                        pro_sub = Button("Prompt Image")

                    with gr.Column(variant="panel", scale=3) as result:
                        itk_ram = State([])
                        itk_res = Gallery(606.406)
                        cap_res = Textbox("Upload an image to get a caption...", 5, 5)
                        pro_res = Textbox("Upload an image to get a prompt...", 5, 5)
                        
                        usc_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=usc_prep,
                            inputs=[itk_img, itk_ram],
                            outputs=[itk_res] 
                        )
                        
                        cfm_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=cfm_prep,
                            inputs=[itk_img, itk_ram],
                            outputs=[itk_res] 
                        )
                        
                        cap_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=client.image_caption,
                            inputs=[itk_img],
                            outputs=[cap_res] 
                        ) 
                        
                        bgr_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=bgr_prep,
                            inputs=[itk_img, itk_ram],
                            outputs=[itk_res] 
                        )
                        
                        pro_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=client.image_prompt,
                            inputs=[itk_img],
                            outputs=[pro_res] 
                        )
                        
                        arc_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=arc_prep,
                            inputs=[itk_img, arc_typ, itk_ram],
                            outputs=[itk_res]
                        )      
                
            with gr.Tab("Image Enhance"):
                
                def ie_prep(ie_img, ie_pro, ie_neg, ie_cre, ie_rsm, ie_hdr, ie_sty, ie_ram):
                    caption = f"{truncate_prompt(ie_pro)} | Creativity: {ie_cre:.2f} | Resemblance: {ie_rsm:.2f} | Style: {ie_sty}"
                    results = client.image_enhance(ie_img, ie_pro, ie_neg, ie_cre, ie_rsm, ie_hdr, ie_sty)
                    if results is not None:
                        ie_ram.insert(0, (results, caption))
                    return ie_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Enhance")
                        Markdown("<center>Basic Settings")
                        ie_img = Image("Upload Image", ["upload"], 199)
                        ie_pro = Textbox("Prompt for image...", lines=1)
                        ie_neg = Textbox("Negative prompt...", lines=1)
                    
                        Markdown("<center>Advanced Settings")
                        with gr.Row():
                            ie_cre = Slider(0.2, 1.0, 0.05, 0.3, "Creativity Strength")
                            ie_rsm = Slider(0.0, 1.0, 0.05, 1.0, "Resemblance Strength")
                        with gr.Row():
                            ie_hdr = Slider(0.0, 1.0, 0.05, 0.0, "HDR Strength")
                        
                        Markdown("<center>Style Presets")
                        ie_sty = Dropdown(sty_styles, sty_styles[0])
                        ie_sub = Button("Generate", "stop")

                    with gr.Column(variant="panel", scale=3) as result:
                        ie_res = Gallery(885.938)
                        ie_ram = State([])
                        ie_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=ie_prep,
                            inputs=[ie_img, ie_pro, ie_neg, ie_cre, ie_rsm, ie_hdr, ie_sty, ie_ram],
                            outputs=[ie_res]
                        )            
                
            with gr.Tab("Object Eraser"):
                
                def oe_prep(oe_mas, oe_ram):
                    caption = f"Object Erased"
                    results = client.image_erase(oe_mas)
                    if results is not None:
                        oe_ram.insert(0, (results, caption))
                    return oe_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Object Eraser")
                        
                        oe_img = Image("Canvas Image", [], 250)
                        with Modal(visible=False) as oe_m1:
                            oe_mas = ImageMask()
                            oe_mas.change(fn=lambda x: x["composite"], inputs=oe_mas, outputs=oe_img)
                            oe_clo = Button("Close Canvas").click(lambda: Modal(visible=False), None, oe_m1)
                        oe_ope = Button("Open Canvas").click(lambda: Modal(visible=True), None, oe_m1)
                    
                        oe_sub = Button("Erase Object", "stop")
                    
                    with gr.Column(variant="panel", scale=3) as result:
                        oe_res = Gallery(885.938)
                        oe_ram = State([])
                        oe_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=oe_prep,
                            inputs=[oe_mas, oe_ram],
                            outputs=[oe_res]
                        ) 
                                
            with gr.Tab("Generative Fill"):
                
                def gf_prep(gf_mas, gf_pro, gf_sty, gf_ram):
                    caption = f"{truncate_prompt(gf_pro)} | Style: {gf_sty}"
                    results = client.image_inpaint(gf_mas, gf_pro, None, gf_sty)
                    if results is not None:
                        gf_ram.insert(0, (results, caption))
                    return gf_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Generative Fill")
                        Markdown("<center>Basic Settings")
                                
                        gf_img = Image("Canvas Image", [], 199)
                        with Modal(visible=False) as gf_m1:
                            gf_mas = ImageMask()
                            gf_mas.change(fn=lambda x: x["composite"], inputs=gf_mas, outputs=gf_img)
                            gf_clo = Button("Close Canvas").click(lambda: Modal(visible=False), None, gf_m1)
                        gf_ope = Button("Open Canvas").click(lambda: Modal(visible=True), None, gf_m1)
                        
                        gf_pro = Textbox("Prompt for image...")

                        Markdown("<center>Style Presets")
                        gf_sty = Dropdown(sty_styles, sty_styles[0])
                        gf_sub = Button("Inpaint Image", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        gf_res = Gallery(885.938)
                        gf_ram = State([])
                        gf_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=gf_prep,
                            inputs=[gf_mas, gf_pro, gf_sty, gf_ram],
                            outputs=[gf_res]
                        )

            with gr.Tab("RT Generator"):
                
                def rtg_prep(rtg_pro, rtg_neg, rtg_siz, rtg_lra, rtg_sed, rtg_sty, rtg_ram):
                    caption = f"{truncate_prompt(rtg_pro)} | Size: {rtg_siz} | LoRA: {rtg_lra} | Style: {rtg_sty}"
                    results = client.realtime_generate(rtg_pro, rtg_neg, rtg_siz, rtg_lra, rtg_sed, rtg_sty)
                    if results is not None:
                        rtg_ram.insert(0, (results, caption))
                    return rtg_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>RT Image Generator")
                        Markdown("<center>Basic Settings")
                        rtg_pro = Textbox("Prompt for image...")
                        rtg_neg = Textbox("Negative prompt...")
                        
                        Markdown("<center>Advanced Settings")
                        with gr.Row():
                            rtg_lra = Dropdown(ime_lora, ime_lora[0], label="LoRA Model")
                            rtg_siz = Dropdown(ime_size, ime_size[0], label="Image Size")
                        
                        rtg_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)
                        
                        Markdown("<center>Style Presets")
                        rtg_sty = Dropdown(sty_styles, sty_styles[0])
                        rtg_sub = Button("Generate", "stop")

                    with gr.Column(variant="panel", scale=3) as result:
                        rtg_res = Gallery(885.938)
                        rtg_ram = State([])
                        rtg_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=rtg_prep,
                            inputs=[rtg_pro, rtg_neg, rtg_siz, rtg_lra, rtg_sed, rtg_sty, rtg_ram],
                            outputs=[rtg_res]
                        )

            with gr.Tab("RT Canvas"):
                
                def rtc_prep(rtc_img, rtc_pro, rtc_neg, rtc_lra, rtc_str, rtc_sed, rtc_sty, rtc_ram):
                    caption = f"{truncate_prompt(rtc_pro)} | LoRA: {rtc_lra} | Strength: {rtc_str:.2f} | Style: {rtc_sty}"
                    results = client.realtime_canvas(rtc_img, rtc_pro, rtc_neg, rtc_lra, rtc_str, rtc_sed, rtc_sty)
                    if results is not None:
                        rtc_ram.insert(0, (results, caption))
                    return rtc_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>RT Canvas")
                        Markdown("<center>Basic Settings")
                        
                        rtc_img = Image("Canvas Image", ['upload'], 199)
                        with Modal(visible=False) as rtc_m1:
                            rtc_can = Paint()
                            rtc_can.change(fn=lambda x: x["composite"], inputs=rtc_can, outputs=rtc_img)
                            rtc_clo = Button("Close Canvas").click(lambda: Modal(visible=False), None, rtc_m1)
                        rtc_ope = Button("Open Canvas").click(lambda: Modal(visible=True), None, rtc_m1)
                        
                        rtc_pro = Textbox("Prompt for image...", lines=1)
                        rtc_neg = Textbox("Negative prompt...", lines=1)
                        
                        Markdown("<center>Advanced Settings")
                        with gr.Row():
                            rtc_lra = Dropdown(ime_lora, ime_lora[0], label="LoRA Model")
                            rtc_str = Slider(0.0, 1.0, 0.1, 1, "Creativity Strength")
                        
                        rtc_sed = Number("Seed (0 Random | -1 CPU)", 0, -1, 1)
                        
                        Markdown("<center>Style Presets")
                        rtc_sty = Dropdown(sty_styles, sty_styles[0])
                        rtc_sub = Button("Generate", "stop")
                    
                    with gr.Column(variant="panel", scale=3) as result:
                        rtc_res = Gallery(885.938)
                        rtc_ram = State([])
                        
                        rtc_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=rtc_prep,
                            inputs=[rtc_img, rtc_pro, rtc_neg, rtc_lra, rtc_str, rtc_sed, rtc_sty, rtc_ram],
                            outputs=[rtc_res]
                        )  

            with gr.Tab("Image Outpaint"):
                def op_prep(op_img, op_siz, op_ram):
                    caption = f"Image Outpaint | Size: {op_siz}"
                    results = client.image_outpaint(op_img, op_siz)
                    if results is not None:
                        op_ram.insert(0, (results, caption))
                    return op_ram
                
                with gr.Row(equal_height=False):
                    with gr.Column(variant="panel", scale=1) as menu:
                        Markdown("## <center>Image Outpaint")
                        Markdown("<center>Basic Settings")
                        op_img = Image("Upload Image", ["upload"], 199)
                    
                        Markdown("<center>Advanced Settings")
                        op_siz = Dropdown(atr_size, atr_size[0], label="Image Size")
                        op_sub = Button("Generate", "stop")
                        
                    with gr.Column(variant="panel", scale=3) as result:
                        op_res = Gallery(885.938)
                        op_ram = State([])
                        op_sub.click(
                            show_progress='minimal',
                            show_api=False,
                            scroll_to_output=True,
                            fn=op_prep,
                            inputs=[op_img, op_siz, op_ram],
                            outputs=[op_res]
                        )
            
            Markdown("<center>Atelier can make mistakes. Check important info. Request errors will return None.")
            Markdown("<center>")

        demo.launch(
            server_name=host,
            server_port=port,
            inbrowser=browser,
            max_file_size=upload_size,
            share=public,
            quiet=quiet
        )
        
    except Exception as e:
        client.logger.error(f"{str(e)}")
        raise