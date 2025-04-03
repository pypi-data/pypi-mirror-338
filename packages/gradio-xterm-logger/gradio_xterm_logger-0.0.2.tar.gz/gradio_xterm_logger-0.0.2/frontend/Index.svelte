<script lang="ts">
	import { JsonView } from "@zerodevx/svelte-json-view";
 	import { onMount, onDestroy } from 'svelte';
	import type { Gradio } from "@gradio/utils";
	import { Block, Info } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import type { SelectData } from "@gradio/utils";
	import { Terminal } from '@xterm/xterm';
	import '@xterm/xterm/css/xterm.css'; // Import Xterm's CSS
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: string[] = []; 
	export let font_size = 14; // Default font size
    export let dark_mode = true; // Default theme
	// Add a reactive block to handle terminal updates
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

	let terminalContainer;
  	let term;

	onMount(() => {
		// Initialize the terminal with props
		term = new Terminal({
			cursorBlink: true,
			fontSize: font_size,  // Use prop value
			theme: {
				background: dark_mode ? '#000000' : '#ffffff',
				foreground: dark_mode ? '#ffffff' : '#000000'
			}
		});

		// Attach the terminal to the DOM
		term.open(terminalContainer);
	});

	let previousValue: string[] = [];

	const arraysEqual = (a: string[], b: string[]): boolean => {
		if (a.length !== b.length) return false;
		for (let i = 0; i < a.length; i++) {
		if (a[i].trim() !== b[i].trim()) return false; // Compare trimmed lines
		}
		return true;
	};

	$: if (term && value) {
    if (!arraysEqual(value, previousValue)) {
      term.clear();
      
      value.forEach(line => {
        // Add proper line formatting
        term.write(`\x1B[90m\x1B[0m ${line.trim()}\r\n`);
      });
      
      previousValue = [...value];
    }
  	}
	// Clean up the terminal when the component is destroyed
	onDestroy(() => {
		if (term) {
		term.dispose();
		}
	});
</script>

<!-- Container for the terminal -->


<style>
  /* Optional: Add custom styles */
  .terminal-container {
    height: 400px; /* Set a fixed height */
    width: 100%;
  }
</style>

<div bind:this={terminalContainer} class="terminal-container" />

