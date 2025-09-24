<script setup>
import { ref } from 'vue';
import timedays from '../../parseddata/timedays.json';

const revealed = ref(Array(timedays.length).fill(false));

function toggle(index) {
	revealed.value[index] = !revealed.value[index];
}
</script>

<template>
	<div v-for="(timeday, idx) in timedays"
		 :key="timeday.suuid"
		 class="flex flex-col gap-1 p-3 mb-3 w-fit bg-slate-500 rounded">
		<div>
			<h3 class="font-semibold cursor-pointer"
				@click="toggle(idx)">
				{{ timeday.day }}
			</h3>
			<p v-if="revealed[idx]"
			   class="text-yellow-200">data</p>
		</div>
	</div>
</template>
