<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <span class="mr-2 headline">CSS - Calcula Simple Sheet</span>
    </v-app-bar>
    <v-content>
      <v-container fluid>
        <v-row>
          <v-col 
            cols="12"
            md="4"
            lg="4"
            xl="4"
          >
            <v-card color="primary">
              <v-card-title>Gere os dados para os cálculos</v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="qtdNumeros"
                      label="Quantidade de números"
                      required
                    />
                  </v-col>
                  <v-col cols="12">
                    <v-range-slider
                      v-model="range"
                      :max="max"
                      :min="min"
                      hide-details
                      class="align-center"
                      color="black"
                    >
                      <template v-slot:prepend>
                        <v-text-field
                          v-model="range[0]"
                          class="mt-0 pt-0"
                          hide-details
                          single-line
                          type="number"
                          style="width: 60px"
                        ></v-text-field>
                      </template>
                      <template v-slot:append>
                        <v-text-field
                          v-model="range[1]"
                          class="mt-0 pt-0"
                          hide-details
                          single-line
                          type="number"
                          style="width: 60px"
                        ></v-text-field>
                      </template>
                    </v-range-slider>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col 
            cols="12"
            md="8"
            lg="8"
            xl="8"
          ></v-col>
        </v-row>
      </v-container>
    </v-content>
    <v-footer
      color="primary"
      app
    >
      <span class="white--text">&copy;
        {{ (new Date()).getFullYear() }}
        <strong>Fatec São José dos Campos</strong>
      </span>
    </v-footer>
  </v-app>
</template>

<script>


export default {
  name: 'App',

  components: {
  },

  data: () => ({
    //
    qtdNumeros: 0,
    min: -1000,
    max: 1000,
    slider: 10,
    range: [-20, 70]
  }),
};
</script>
