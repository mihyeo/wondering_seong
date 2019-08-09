console.clear();
(function() {
'use strict';
customElements.define('photo-slider', class extends HTMLElement {
  static get observedAttributes() {
    return ['selected'];
  }
  constructor() {
    super(); // always always
    this.attachShadow({mode: 'open'});
  }
  attributeChangedCallback(attrName, oldVal, newVal) {
    if (oldVal !== newVal) {
      if (attrName === 'selected') this._selectedChanged(newVal);
    }
  }
  set selected(val) {
    if (this._selected) this._selected.removeAttribute('selected');
    const oldSelected = this._selected;
    this._selected = val;
    this._selected.setAttribute('selected', '');
    this._selectedChanged(val, oldSelected);
  }
  get selected() {
    return this._selected;
  }
  connectedCallback() {
    this.shadowRoot.innerHTML = `
    <style>
      :host {
        display: block;
        position: relative;
        overflow: hidden;
      }
      div > ::slotted(:not([selected])) {
        display: none;
      }
      button {
        position: absolute;
        top: calc(50% - 20px);
        padding: 0;
        line-height: 40px;
        border: none;
        background: none;
        color: #DDD;
        font-size: 40px;
        font-weight: bold;
        opacity: 0.7;
      }
      button:hover,
      button:focus {
        opacity: 1;
      }
      #prevBtn {
        left: 12px;
      }
      #nextBtn {
        right: 12px;
      }
      button[disabled] {
        opacity: 0.4;
      }
    </style>
    <div id="photo-slider__div">
      <slot></slot>
    </div>
    <button id="prevBtn">&#x276E;</button>
    <button id="nextBtn">&#x276F;</button>
    `;
    this.$ = {};
    this.$.prevBtn = this.shadowRoot.querySelector('#prevBtn');
    this.$.nextBtn = this.shadowRoot.querySelector('#nextBtn');
    this.shadowRoot.addEventListener('slotchange', this._resetSelected);
    this._resetSelected();
    requestAnimationFrame(this._installListeners.bind(this));
  }
   _installListeners() {
    this.addEventListener('transitionend', this._resetChildrenStyles);
    this.addEventListener('touchstart', this._touchstart);
    this.addEventListener('touchmove', this._touchmove);
    this.addEventListener('touchend', this._touchend);
    this.$.nextBtn.addEventListener('click', this.next.bind(this));
    this.$.prevBtn.addEventListener('click', this.previous.bind(this));
  }
  _resetChildrenStyles() {
    let elem = this.firstElementChild;
    while (elem) {
      elem.style.display = '';
      elem.style.transition = '';
      elem.style.transform = '';
      elem = elem.nextElementSibling;
    }
  }
  previous() {
    const elem = this.selected && this.selected.previousElementSibling;
    if (elem && !this._touchDir) {
      // Setup transition start state
      const oldSelected = this.selected;
      this._translateX(oldSelected, 0);
      this._translateX(elem, -this.offsetWidth);
      // Start the transition
      this.selected = elem;
      this._translateX(oldSelected, this.offsetWidth, true /* transition */);
      this._translateX(elem, 0, true /* transition */);
    }
  }
  next() {
    const elem = this.selected && this.selected.nextElementSibling;
    if (elem && !this._touchDir) {
      // Setup transition start state
      const oldSelected = this.selected;
      this._translateX(oldSelected, 0);
      this._translateX(elem, this.offsetWidth);
      // Start the transition
      this.selected = elem;
      this._translateX(oldSelected, -this.offsetWidth, true /* transition */);
      this._translateX(elem, 0, true /* transition */);
    }
  }

  _loadImage(img) {
    if (img && !img.src) {
      img.src = img.getAttribute('data-src');
    }
  }

  _selectedChanged(selected, oldSelected) {
    if (oldSelected) oldSelected.removeAttribute('selected');
    if (selected) selected.setAttribute('selected', '');
    if (selected) {
      this.$.prevBtn.disabled = !selected.previousElementSibling;
      this.$.nextBtn.disabled = !selected.nextElementSibling;
      this._loadImage(selected);
      this._loadImage(selected.previousElementSibling);
      this._loadImage(selected.nextElementSibling);
    } else {
      this.$.prevBtn.disabled = true;
      this.$.nextBtn.disabled = true;
    }
  }
  _resetSelected() {
    if (!this.selected || this.selected.parentElement !== this) {
      this.selected = this.firstElementChild;
    }
  }
  _translateX(elem, x, transition) {
    elem.style.display = 'block';
    elem.style.transition = transition ? 'transform 0.2s' : '';
    elem.style.transform = 'translate3d(' + x + 'px, 0, 0)';
  }
  _touchstart(event) {
    if (this.childElementCount < 2) return;
    if (!this._touchDir) {
      this._startX = event.changedTouches[0].clientX;
      this._startY = event.changedTouches[0].clientY;
    }
  }
  _touchmove(event) {
    if (this.childElementCount < 2) return;
    // Is touchmove mostly horizontal or vertical?
    if (!this._touchDir) {
      const absX = Math.abs(event.changedTouches[0].clientX - this._startX);
      const absY = Math.abs(event.changedTouches[0].clientY - this._startY);
      this._touchDir = absX > absY ? 'x' : 'y';
    }
    if (this._touchDir === 'x') {
      // Prevent vertically scrolling when swiping
      event.preventDefault();

      let dx = Math.round(event.changedTouches[0].clientX - this._startX);
      const prevChild = this.selected.previousElementSibling;
      const nextChild = this.selected.nextElementSibling;

      // Don't translate past the current image if there's no adjacent image in that direction
      if ((!prevChild && dx > 0) || (!nextChild && dx < 0)) {
        dx = 0;
      }

      this._translateX(this.selected, dx);
      if (prevChild) {
        this._translateX(prevChild, dx - this.offsetWidth);
      }
      if (nextChild) {
        this._translateX(nextChild, dx + this.offsetWidth);
      }
    }
  }
  _touchend(event) {
    if (this.childElementCount < 2) return;
    // Don't finish swiping if there are still active touches.
    if (event.touches.length) return;

    if (this._touchDir === 'x') {
      let dx = Math.round(event.changedTouches[0].clientX - this._startX);
      const prevChild = this.selected.previousElementSibling;
      const nextChild = this.selected.nextElementSibling;

      // Don't translate past the current image if there's no adjacent image in that direction
      if ((!prevChild && dx > 0) || (!nextChild && dx < 0)) {
        dx = 0;
      }

      if (dx > 0) {
        if (dx > 100) {
          if (dx === this.offsetWidth) {
            // No transitionend will fire (since we're already in the final state),
            // so reset children styles now
            this._resetChildrenStyles();
          } else {
            this._translateX(prevChild, 0, true);
            this._translateX(this.selected, this.offsetWidth, true);
          }
          this.selected = prevChild;
        } else {
          this._translateX(prevChild, -this.offsetWidth, true);
          this._translateX(this.selected, 0, true);
        }
      } else if (dx < 0) {
        if (dx < -100) {
          if (dx === -this.offsetWidth) {
            // No transitionend will fire (since we're already in the final state),
            // so reset children styles now
            this._resetChildrenStyles();
          } else {
            this._translateX(this.selected, -this.offsetWidth, true);
            this._translateX(nextChild, 0, true);
          }
          this.selected = nextChild;
        } else {
          this._translateX(this.selected, 0, true);
          this._translateX(nextChild, this.offsetWidth, true);
        }
      } else {
        // No transitionend will fire (since we're already in the final state),
        // so reset children styles now
        this._resetChildrenStyles();
      }
    }
    // Reset touch direction
    this._touchDir = null;
  }
});
})();