const port = chrome.runtime.connectNative("albania_ads_blocker");

port.onMessage.addListener((response) => {
  if (response.blocked) {
    console.log("Ad blocked:", response);
  }
});

chrome.webRequest.onBeforeRequest.addListener(
  (details) => {
    port.postMessage({ url: details.url });
  },
  { urls: ["<all_urls>"] },
  ["blocking"]
);
