
class BioPoolAdvancedCard extends HTMLElement {
  set hass(hass) {
    const state = hass.states["sensor.biopool_status"];
    if (!state) {
      this.innerHTML = "<ha-card><div style='padding: 16px;'>BioPool Status not available</div></ha-card>";
      return;
    }

    const mode = state.state;
    const temp = state.attributes.temperature ?? "N/A";
    const runtime = state.attributes.runtime_hours ?? 0;
    const uv = state.attributes.uv_level ?? 0;
    const oxybio = state.attributes.oxybio_level ?? 0;
    const biobacter = state.attributes.biobacter_level ?? 0;

    this.innerHTML = `
      <ha-card header="BioPool-NewGen">
        <div style="padding: 16px; display: flex; flex-direction: column; gap: 12px;">
          <div><strong>Mode:</strong> ${mode}</div>
          <div><strong>Température:</strong> ${temp} °C</div>
          <div><strong>Filtration aujourd'hui:</strong> ${runtime} h</div>

          <div><strong>Consommables:</strong></div>
          <div>UV: <progress value="${uv}" max="100"></progress> ${uv}%</div>
          <div>Oxybio: <progress value="${oxybio}" max="100"></progress> ${oxybio}%</div>
          <div>BioBacter: <progress value="${biobacter}" max="100"></progress> ${biobacter}%</div>

          <div style="display: flex; gap: 8px; margin-top: 12px;">
            <mwc-button @click="this._callService(hass, 'auto')">Auto</mwc-button>
            <mwc-button @click="this._callService(hass, 'boost')">Boost</mwc-button>
            <mwc-button @click="this._callService(hass, 'off')">Stop</mwc-button>
          </div>
        </div>
      </ha-card>
    `;
  }

  _callService(hass, mode) {
    hass.callService("biopool_newgen", "set_mode", {
      mode: mode
    });
  }

  setConfig(config) {}
  getCardSize() { return 3; }
}

customElements.define("biopool-advanced-card", BioPoolAdvancedCard);
