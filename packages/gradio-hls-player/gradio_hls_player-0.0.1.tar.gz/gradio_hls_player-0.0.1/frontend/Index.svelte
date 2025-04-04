<script lang="ts">
    import { onMount, onDestroy, afterUpdate } from 'svelte';
    import type { Gradio } from "@gradio/utils";
    import { Block, Info } from "@gradio/atoms";
    import { StatusTracker } from "@gradio/statustracker";
    import type { LoadingStatus } from "@gradio/statustracker";
    import type { SelectData } from "@gradio/utils";

    export let elem_id = "";
    export let elem_classes: string[] = [];
    export let visible = true;
    export let value: {
        url: string;
        width: number;
        height: number;
        autoplay: boolean;
        hide_player_control_bar: boolean;
    } = {
        url: "",
        width: 640,
        height: 360,
        autoplay: false,
        hide_player_control_bar: false
    };
    export let container = true;
    export let scale: number | null = null;
    export let min_width: number | undefined = undefined;
    export let loading_status: LoadingStatus;
    export let gradio: Gradio<{
        change: never;
        select: SelectData;
        input: never;
        clear_status: LoadingStatus;
    }>;

    let videoElement: HTMLVideoElement;
    let hlsInstance: any = null;
    let isLoading = true;
    let errorState = false;

    const initializeHLS = async (url: string) => {
        try {
            if (!window.Hls) {
                await loadHlsLibrary();
            }

            if (Hls.isSupported()) {
                hlsInstance = new Hls();
                hlsInstance.loadSource(url);
                hlsInstance.attachMedia(videoElement);
                
                hlsInstance.on(Hls.Events.MANIFEST_PARSED, () => {
                    console.log('Manifest parsed');
                    isLoading = false;
                });
                
                hlsInstance.on(Hls.Events.ERROR, (event, data) => {
                    console.error('HLS Error:', data);
                    errorState = true;
                    isLoading = false;
                });
            } else if (videoElement.canPlayType('application/vnd.apple.mpegurl')) {
                videoElement.src = url;
                videoElement.addEventListener('loadedmetadata', () => {
                    isLoading = false;
                });
            } else {
                console.error('HLS not supported');
                errorState = true;
                isLoading = false;
            }
        } catch (error) {
            console.error('Initialization failed:', error);
            errorState = true;
            isLoading = false;
        }
    };

    const loadHlsLibrary = () => {
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/hls.js@latest';
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        });
    };

    onMount(() => {
        if (value.url) initializeHLS(value.url);
    });

    afterUpdate(() => {
        if (value.url && videoElement) {
            if (hlsInstance) hlsInstance.destroy();
            initializeHLS(value.url);
        }
    });

    onDestroy(() => {
        if (hlsInstance) {
            hlsInstance.destroy();
        }
    });
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
    {#if loading_status}
        <StatusTracker
            autoscroll={gradio.autoscroll}
            i18n={gradio.i18n}
            {loading_status}
            on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
        />
    {/if}

    {#if value.url}
        <div style="margin: 10px 0;">
            {#if isLoading}
                <div class="loading">Loading HLS stream...</div>
            {:else if errorState}
                <div class="error">Failed to load stream</div>
            {/if}
        </div>
        
        <video 
            bind:this={videoElement} 
            width={value.width}     
            height={value.height}    
            autoplay={value.autoplay}
            controls={!value.hide_player_control_bar}
            style="background: black; border: 1px solid #666;"
            on:error={(e) => console.error('Video error:', e)}
        >
            <track
                kind="captions"
                label="Automatic Captions"
                src="data:text/vtt;base64,"
                default
            />
        </video>
    {:else}
        <Info>Invalid HLS stream URL</Info>
    {/if}
</Block>

<style>
    .loading { color: #2196F3; }
    .error { color: #f44336; }
</style>